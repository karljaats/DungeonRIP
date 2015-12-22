import random
from map_objects import *


class Map:
    def __init__(self, images):
        self.map = None
        self.images = images
        self.width = 0
        self.height = 0

    def generate_map(self, size_x, size_y):
        self.width = size_x
        self.height = size_y

        self.map = []
        for x in range(0, size_x):
            self.map.append([])
            for y in range(0, size_y):
                if x == 50 and y == 50:
                    self.map[x].append(Floor(x, y, self.images["floor"]))
                else:
                    type = random.randint(0, 1)  # 0 - wall, 1 - floor
                    if type == 0:
                        self.map[x].append(Wall(x, y, self.images["wall"]))
                    elif type == 1:
                        self.map[x].append(Floor(x, y, self.images["floor"]))
