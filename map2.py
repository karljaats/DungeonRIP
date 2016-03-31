import random


class Map:
    def __init__(self, images):
        self.map = None
        self.images = images
        self.width = 0
        self.height = 0
        self.level = 1  # praegune sügavuse raske

        self.objects = {
            "wall": {
                "image": images["wall"],
                "passable": False,
                "diggable": True
            },
            "floor": {
                "image": images["floor"],
                "passable": True,
                "diggable": False
            },
            "stair_up": {
                "image": images["stair_up"],
                "passable": True,
                "diggable": False
            },
            "stair_down": {
                "image": images["stair_down"],
                "passable": True,
                "diggable": False
            }
        }

    def generate_map(self, size_x=100, size_y=100):
        """
        genereerib listi tile_type-idest, mis representeerib kaarti
        :param size_x: kaardi suurus tile-ides
        :param size_y: kaardi suurus tile-ides
        :return: Mängija algpositsioon
        """
        self.width = size_x
        self.height = size_y

        # Palju katseid teha
        tries = 100

        self.map = []
        gen_points = []  # punktid, kust genereeritakse uusi ruume

        # tee list ning täida see seintega
        for x in range(self.width):
            self.map.append([])
            for y in range(self.height):
                self.map[x].append("wall")

        # loo algne ruum
        dimensions = [random.randint(4, 10), random.randint(4, 10)]
        pos = [random.randint(self.width//2 - 20, self.width//2 + 20), random.randint(self.height//2 - 20, self.height//2 + 20)]
        self.fill(pos, dimensions, "floor")
        player_pos = [random.randint(pos[0], pos[0] + dimensions[0]-1), random.randint(pos[1], pos[1] + dimensions[1]-1)]
        gen_points = self.generate_gen_points(gen_points, pos, dimensions, random.randint(1, 6))

        # genereeri ülejäänud kaart
        for i in range(tries):
            pass

        return player_pos

    def fill(self, pos, dimensions, tile_type):
        """
        Täidab määratud ala määratud tile_type-ga alates pos-ist(kaasa arvatud)
        :param pos: algpunkt(kaasa arvatud)
        :param dimensions: filli dimensioonid
        :param tile_type: tile_type milleks ala muuta
        """
        for x in range(0, dimensions[0]):
            for y in range(0, dimensions[1]):
                self.map[x+pos[0]][y+pos[1]] = tile_type

    def generate_gen_points(self, gen_points, room_pos, room_dimensions, number_of_points):
        """
        Genereerib kindla arvu punkte antud ruumi seintes kust generatsioon saab jätkuda
        :param gen_points: list kogu kaardi generatsiooni punktidest
        :param room_pos: ruumi kõige ülemise vasakpoolsema floor tile'i asukoht
        :param room_dimensions: ruumi põranda positsioon
        :param number_of_points: genereeritavate punktide arv
        :return: uuendatud gen_points, nüüd ka selle ruumi punktidega
        """
        room_pos[0] -= 1
        room_pos[1] -= 1
        for i in range(number_of_points):
            while True:
                point = [random.randint(0, room_dimensions[0]+1), random.randint(0, room_dimensions[1]+1)]
                # kui punkt pole nurga seintes
                if point not in [[0, 0], [0, room_dimensions[1]+1], [room_dimensions[0]+1, 0], [room_dimensions[0]+1, room_dimensions[1]+1]]:
                    # kui tile on wall tüüpi
                    if self.map[point[0] + room_pos[0]][point[1] + room_pos[1]] == "wall":
                        # kui juba pole gen_pointi selle punkti kõrval
                        if [point[0]+room_pos[0], point[1]+room_pos[1]] not in gen_points or \
                                    [point[0]+room_pos[0]-1, point[1]+room_pos[1]] not in gen_points or \
                                    [point[0]+room_pos[0]+1, point[1]+room_pos[1]] not in gen_points or \
                                    [point[0]+room_pos[0], point[1]+room_pos[1]-1] not in gen_points or \
                                    [point[0]+room_pos[0], point[1]+room_pos[1]+1] not in gen_points:
                            gen_points.append([point[0]+room_pos[0], point[1]+room_pos[1]])
                            break
        return gen_points
