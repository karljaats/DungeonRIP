class Floor:
    def __init__(self, x, y, img):
        self.image = img
        self.x = x  # in map coordinates, not screen ones
        self.y = y
        self.passable = True  # can you walk on it
        self.diggable = False


class Wall:
    def __init__(self, x, y, img):
        self.image = img
        self.x = x  # in map coordinates, not screen ones
        self.y = y
        self.passable = False  # can you walk on it
        self.diggable = True


class OuterWall:
    def __init__(self, x, y, img):
        self.image = img
        self.x = x  # in map coordinates, not screen ones
        self.y = y
        self.passable = False  # can you walk on it
        self.diggable = False