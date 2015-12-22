import pygame


class Player():
    def __init__(self, x, y, images):
        self.image = images["player"]
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        self.x = x  # in map coordinates, not screen ones
        self.y = y

        self.max_health = 10
        self.current_health = self.max_health

    def move(self, dif_x, dif_y, map):
        if map.map[self.x + dif_x][self.y + dif_y].passable \
                and map.width > self.x + dif_x >= 0 and map.height > self.y + dif_y >= 0:
            self.x += dif_x
            self.y += dif_y
            return True  # if camera should be moved
        else:
            return False
