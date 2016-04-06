import pygame


class Character:
    def __init__(self, x, y, images, name):
        self.image = images[name]
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        self.x = x  # tiledes, mitte pixlites
        self.y = y

        self.max_health = 10
        self.current_health = self.max_health
        self.attack = 1

    def damage(self, damage):
        self.current_health -= damage
