import random


class Map:
    def __init__(self, images):
        self.map = None
        self.images = images
        self.width = 0
        self.height = 0

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
            }
        }

    def generate_map(self, size_x=100, size_y=100):
        self.width = size_x
        self.height = size_y

        # how many tries should be made
        tries = 100

        self.map = []
        gen_points = []  # point from where to generate new stuff from

        # initiate the list and fill everything with wall
        for x in range(self.width):
            self.map.append([])
            for y in range(self.height):
                self.map[x].append("wall")

        # create center room
        dimensions = [random.randint(4, 10), random.randint(4, 10)]
        pos = [random.randint(self.width//2 - 20, self.width//2 + 20), random.randint(self.height//2 - 20, self.height//2 + 20)]
        self.fill(pos, dimensions, "floor")
        player_pos = [random.randint(pos[0], pos[0] + dimensions[0]), random.randint(pos[1], pos[1] + dimensions[1])]
        gen_points = self.generate_gen_points(gen_points, pos, dimensions, random.randint(1, 6))

        # create the map
        for i in range(tries):
            pass

        return player_pos

    def fill(self, pos, dimensions, tile_type):
        for x in range(0, dimensions[0]):
            for y in range(0, dimensions[1]):
                self.map[x+pos[0]][y+pos[1]] = tile_type

    def generate_gen_points(self, gen_points, room_pos, room_dimensions, number_of_points):
        room_pos[0] -= 1
        room_pos[1] -= 1
        for i in range(number_of_points):
            while True:
                point = [random.randint(0, room_dimensions[0]+1), random.randint(0, room_dimensions[1]+1)]
                if point not in [[0, 0], [0, room_dimensions[1]+1], [room_dimensions[0]+1, 0], [room_dimensions[0]+1, room_dimensions[1]+1]]:
                    if self.map[point[0] + room_pos[0]][point[1] + room_pos[1]] == "wall":
                        gen_points.append([point[0]+room_pos[0], point[1]+room_pos[1]])
                        break
                        # FIXME
                        # check if gen_point already exists and that it's not next to another one
        return gen_points
