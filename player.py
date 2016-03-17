import pygame


class Player:
    def __init__(self, x, y, images):
        self.image = images["player"]
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        self.x = x  # in map coordinates, not screen ones
        self.y = y

        self.max_health = 10
        self.current_health = self.max_health

    def move(self, dif_x, dif_y, map):
        if map.objects[map.map[self.x + dif_x][self.y + dif_y]]["passable"]:
            self.x += dif_x
            self.y += dif_y
