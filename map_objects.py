import pygame


class Floor():
    def __init__(self, x, y, img):
        self.image = img
        self.x = x  # in map coordinates, not screen ones
        self.y = y
        self.passable = True  # can you walk on it


class Wall():
    def __init__(self, x, y, img):
        self.image = img
        self.x = x  # in map coordinates, not screen ones
        self.y = y
        self.passable = False  # can you walk on it
