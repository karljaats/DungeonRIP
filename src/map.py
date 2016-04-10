import random


class Map:
    def __init__(self, images):
        self.map = None
        self.visibility_map = None
        self.images = images
        self.width = 0
        self.height = 0
        self.level = 1  # praegune sügavuse raske

        self.objects = {
            "wall": {
                "image": images["wall"],
                "passable": False
            },
            "floor": {
                "image": images["floor"],
                "passable": True
            },
            "stair_up": {
                "image": images["stair_up"],
                "passable": True
            },
            "stair_down": {
                "image": images["stair_down"],
                "passable": True
            },
            "enclosed_wall": {
                "image": images["black"],
                "passable": False
            }
        }

    def generate_map(self, size_x=100, size_y=100):
        """
        genereerib listi tile_type-idest, mis representeerib kaarti
        :param size_x: kaardi suurus tile-ides
        :param size_y: kaardi suurus tile-ides
        :return: Mängija algpositsioon
        """
        try:
            self.width = size_x
            self.height = size_y

            # Palju katseid teha
            tries = 100

            self.map = []
            gen_points = []  # punktid, kust genereeritakse uusi ruume

            feature_list = self.create_feature_list()

            # tee list ning täida see seintega
            for p in range(self.width):
                self.map.append([])
                for q in range(self.height):
                    self.map[p].append("wall")

            # tee algne visibility_map
            self.visibility_map = []
            for p in range(self.width):
                self.visibility_map.append([])
                for q in range(self.height):
                    self.visibility_map[p].append(False)

            # loo algne ruum
            dimensions = [random.randint(4, 10), random.randint(4, 10)]
            pos = [random.randint(self.width//2 - 20, self.width//2 + 20), random.randint(self.height//2 - 20, self.height//2 + 20)]
            self.fill(pos, dimensions, "floor")
            player_pos = [random.randint(pos[0], pos[0] + dimensions[0]-1), random.randint(pos[1], pos[1] + dimensions[1]-1)]
            gen_points = self.generate_gen_points(gen_points, pos, dimensions)

            # genereeri ülejäänud kaart
            for a in range(tries):
                point = gen_points[random.randint(0, len(gen_points)-1)]
                x = point[0]
                y = point[1]

                feature = feature_list[random.randint(0, len(feature_list)-1)]

                # leia suund
                if self.map[x+1][y] == "floor":
                    direction = "W"
                elif self.map[x-1][y] == "floor":
                    direction = "E"
                elif self.map[x][y+1] == "floor":
                    direction = "N"
                elif self.map[x][y-1] == "floor":
                    direction = "S"

                if feature == "room":
                    feature_width = random.randint(4, 10)
                    feature_height = random.randint(4, 10)
                elif feature == "corridor":
                    if direction == "N" or direction == "S":
                        feature_width = 1
                        feature_height = random.randint(4, 15)
                    if direction == "E" or direction == "W":
                        feature_width = random.randint(4, 15)
                        feature_height = 1

                if feature == "corridor":
                    corridor_length = 0
                    if direction == "N":
                        top_left = [x, y-feature_height+1]
                        for i in range(feature_height):
                            if y-i > 0:
                                self.map[x][y-i] = "floor"
                                self.add_to_visibility_map([x, y-i])
                                corridor_length += 1
                                if self.map[x-1][y-i-1] != "wall" or self.map[x][y-i-1] != "wall" or self.map[x+1][y-i-1] != "wall":
                                    top_left = [x, y-i]
                                    break
                    elif direction == "E":
                        top_left = [x, y]
                        for i in range(feature_width):
                            if x+i < self.width-1:
                                self.map[x+i][y] = "floor"
                                self.add_to_visibility_map([x+i, y])
                                corridor_length += 1
                                if self.map[x+i+1][y-1] != "wall" or self.map[x+i+1][y] != "wall" or self.map[x+i+1][y+1] != "wall":
                                    break
                    elif direction == "S":
                        top_left = [x, y]
                        for i in range(feature_height):
                            if y+i < self.height-1:
                                self.map[x][y+i] = "floor"
                                self.add_to_visibility_map([x, y+i])
                                corridor_length += 1
                                if self.map[x-1][y+i+1] != "wall" or self.map[x][y+i+1] != "wall" or self.map[x+1][y+i+1] != "wall":
                                    break
                    elif direction == "W":
                        top_left = [x-feature_width+1, y]
                        for i in range(feature_width):
                            if x-i > 0:
                                self.map[x-i][y] = "floor"
                                self.add_to_visibility_map([x-i, y])
                                corridor_length += 1
                                if self.map[x-i-1][y-1] != "wall" or self.map[x-i-1][y] != "wall" or self.map[x-i-1][y+1] != "wall":
                                    top_left = [x-i, y]
                                    break

                    gen_points.remove(point)
                    if corridor_length > 3:
                        if direction == "W" or direction == "E":
                            gen_points = self.generate_gen_points(gen_points, top_left, [corridor_length, 1])
                        else:
                            gen_points = self.generate_gen_points(gen_points, top_left, [1, corridor_length])

                elif feature == "room":
                    # leia uue toa ülemise vasaku põranda koordinaadid
                    if direction == "N":
                        top_left = [x-random.randint(0, feature_width-1), y-feature_height]
                    elif direction == "E":
                        top_left = [x+1, y-random.randint(0, feature_height-1)]
                    elif direction == "S":
                        top_left = [x-random.randint(0, feature_width-1), y+1]
                    elif direction == "W":
                        top_left = [x-feature_width, y-random.randint(0, feature_height-1)]

                    # kas ruum jääb kaardi sisse
                    if not 0 < top_left[0] < self.width or not 0 < top_left[1] < self.height or not 0 < top_left[0]\
                            + feature_width < self.width or not 0 < top_left[1] + feature_height < self.height:
                        continue

                    enough_room = True
                    for k in range(feature_width+2):
                        for j in range(feature_height+2):
                            if self.map[top_left[0]-1+k][top_left[1]-1+j] != "wall":
                                enough_room = False
                                break
                        if not enough_room:
                            break

                    if not enough_room:
                        continue

                    # pane ruum kaardile
                    self.map[x][y] = "floor"  # uksekoht
                    self.add_to_visibility_map([x, y])
                    self.fill(top_left, [feature_width, feature_height], "floor")

                    gen_points.remove(point)
                    gen_points = self.generate_gen_points(gen_points, top_left, [feature_width, feature_height])

            # muuda kõik täielikult ligipääsmatud seinad mustaks
            for x in range(self.width):
                for y in range(self.height):
                    if not self.visibility_map[x][y]:
                        self.map[x][y] = "enclosed_wall"

            # genereeri treppe
            for i in range(2):
                while True:
                    stair_pos = [random.randint(0, self.width-1), random.randint(0, self.height-1)]
                    if self.map[stair_pos[0]][stair_pos[1]] == "floor":
                        self.map[stair_pos[0]][stair_pos[1]] = "stair_down"
                        break
                if self.level > 1:
                    while True:
                        stair_pos = [random.randint(0, self.width-1), random.randint(0, self.height-1)]
                        if self.map[stair_pos[0]][stair_pos[1]] == "floor":
                            self.map[stair_pos[0]][stair_pos[1]] = "stair_up"
                            break

            return player_pos
        except IndexError:
            print("Map generation failed")
            return self.generate_map(size_x, size_y)

    def fill(self, pos, dimensions, tile_type):
        """
        Täidab määratud ala määratud tile_type-ga alates pos-ist(kaasa arvatud)
        :param pos: algpunkt(kaasa arvatud)
        :param dimensions: filli dimensioonid
        :param tile_type: tile_type milleks ala muuta
        :return: None
        """
        for x in range(0, dimensions[0]):
            for y in range(0, dimensions[1]):
                self.map[x+pos[0]][y+pos[1]] = tile_type
                if tile_type == "floor":
                    self.add_to_visibility_map([x+pos[0], y+pos[1]])

    def generate_gen_points(self, gen_points, room_pos, room_dimensions):
        """
        Genereerib kindla arvu punkte antud ruumi seintes kust generatsioon saab jätkuda
        :param gen_points: list kogu kaardi generatsiooni punktidest
        :param room_pos: ruumi kõige ülemise vasakpoolsema floor tile'i asukoht
        :param room_dimensions: ruumi põranda positsioon
        :return: uuendatud gen_points, nüüd ka selle ruumi punktidega
        """
        number_of_points = random.randint(2, 6)
        room_pos[0] -= 1
        room_pos[1] -= 1
        for i in range(number_of_points):
            count = 0
            while count < 100:
                count += 1
                point = [random.randint(0, room_dimensions[0]+1), random.randint(0, room_dimensions[1]+1)]
                # kui punkt pole nurga seintes
                if point not in [[0, 0], [0, room_dimensions[1]+1], [room_dimensions[0]+1, 0], [room_dimensions[0]+1, room_dimensions[1]+1]]:
                    # kui tile on wall tüüpi
                    if self.map[point[0] + room_pos[0]][point[1] + room_pos[1]] == "wall":
                        # kui juba pole gen_pointi selle punkti kõrval
                        if [point[0]+room_pos[0], point[1]+room_pos[1]] not in gen_points and \
                                    [point[0]+room_pos[0]-1, point[1]+room_pos[1]] not in gen_points and \
                                    [point[0]+room_pos[0]+1, point[1]+room_pos[1]] not in gen_points and \
                                    [point[0]+room_pos[0], point[1]+room_pos[1]-1] not in gen_points and \
                                    [point[0]+room_pos[0], point[1]+room_pos[1]+1] not in gen_points:
                            gen_points.append([point[0]+room_pos[0], point[1]+room_pos[1]])
                            break
        return gen_points

    def create_feature_list(self):
        """
        Teeb listi võimalikest struktuuridest nende esinemise tõenäosuse järgi, et kasutada koos
        random number generaatoriga
        :return: list õiges suhtes korduvate featuritest
        """
        feature_list = []

        # ei pea kokku andma 100
        probabilities = {
                    "room": 70,
                    "corridor": 30
                }

        for feature in probabilities:
            for i in range(probabilities[feature]):
                feature_list.append(feature)

        return feature_list

    def add_to_visibility_map(self, pos):
        """
        Muudab kõik antud tile ja selle ümber oleva nähtavaks
        :param pos: tile positsioon
        :return: None
        """
        x = pos[0]
        y = pos[1]

        self.visibility_map[x-1][y-1] = True
        self.visibility_map[x-1][y] = True
        self.visibility_map[x-1][y+1] = True
        self.visibility_map[x][y-1] = True
        self.visibility_map[x][y] = True
        self.visibility_map[x][y+1] = True
        self.visibility_map[x+1][y-1] = True
        self.visibility_map[x+1][y] = True
        self.visibility_map[x+1][y+1] = True

    def generate_monster(self, camera):
        """
        Genereerib ühe kolli
        :return: kolli asukoht
        """
        pos = [0, 0]
        while True:
            pos = [random.randint(0, self.width-1), random.randint(0, self.height-1)]
            if (pos[0] < camera.x or pos[0] > camera.x + camera.width) and (pos[1] < camera.y or pos[1] > camera.y + camera.height):
                if self.map[pos[0]][pos[1]] == "floor":
                    break
        return pos