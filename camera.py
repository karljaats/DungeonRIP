import pygame


class Camera:
    def __init__(self, x, y, screen, tile_size):
        self.x = x
        self.y = y
        self.width = screen.get_width()//tile_size
        self.height = screen.get_height()//tile_size
        self.tile_size = tile_size

        self.disposition_x = 0
        self.disposition_y = 0

    def draw(self, map, characters):
        surface = pygame.Surface((self.width * self.tile_size, self.height * self.tile_size))

        # draw map
        for x in range(0, self.width):
            for y in range(0, self.height):
                object = map.map[self.x + x][self.y + y]  # map object
                destination = ((object.x - self.x)*self.tile_size, (object.y - self.y)*self.tile_size)
                surface.blit(object.image, destination)

        # draw characters
        for dude in characters:
            char = characters[dude]  # object of the characters class
            # Is it on the screen?
            if self.x + self.width > char.x >= self.x and self.y + self.height > char.y >= self.y:
                surface.blit(char.image, ((char.x-self.x)*self.tile_size, (char.y-self.y)*self.tile_size))

        return surface

    def move(self, dif_x, dif_y, map_width, map_height):
        if map_width - self.width > self.x + dif_x >= 0 and self.disposition_x == 0:
            self.x += dif_x
        else:
            self.disposition_x += dif_x

        if map_height - self.height > self.y + dif_y >= 0 and self.disposition_y == 0:
            self.y += dif_y
        else:
            self.disposition_y += dif_y
