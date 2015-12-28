import random
from map_objects import *


class Map:
    def __init__(self, images):
        self.map = None
        self.images = images
        self.width = 0
        self.height = 0

    # taken from http://www.roguebasin.com/index.php?title=Dungeon-Building_Algorithm
    # randomly picks tiles until it finds a wall of a room
    # and puts a random "feature" there if there's room for it
    def generate_map(self, size_x=100, size_y=100, feature_count=300):
        self.width = size_x
        self.height = size_y

        self.map = {}
        # fill everything with wall
        for x in range(0, size_x):
            for y in range(0, size_y):
                if x == 0 or x == size_x-1 or y == 0 or y == size_y-1:
                    self.map[(x, y)] = "outer_wall"
                else:
                    self.map[(x, y)] = "wall"

        # create center room
        width = random.randint(4, 10)
        height = random.randint(4, 10)
        for x in range(0, width):
            for y in range(0, height):
                self.map[(self.width//2 - width//2 + x, self.height//2 - height//2 + y)] = "floor"

        # change names for objects (maybe unneeded)
        for i in self.map:
            name = self.map[i]
            if name == "wall":
                self.map[i] = Wall(i[0], i[1], self.images["wall"])
            elif name == "outer_wall":
                self.map[i] = OuterWall(i[0], i[1], self.images["wall"])
            elif name == "floor":
                self.map[i] = Floor(i[0], i[1], self.images["floor"])
