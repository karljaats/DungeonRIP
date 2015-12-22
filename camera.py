import pygame


class Camera:
    def __init__(self, screen_w, screen_h, tile_size, x=0, y=0):
        self.x = x
        self.y = y
        self.overlay_bottom_h = 6
        self.overlay_side_w = 10
        self.width = screen_w - self.overlay_side_w
        self.height = screen_h - self.overlay_bottom_h
        self.tile_size = tile_size

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

    def center(self, map_width, map_height, player_x, player_y):
        x = player_x - self.width//2
        y = player_y - self.height//2

        if map_width - self.width >= x:
            if x >= 0:
                self.x = x
            else:
                self.x = 0
        else:
            self.x = map_width - self.width

        if map_height - self.height >= y:
            if y >= 0:
                self.y = y
            else:
                self.y = 0
        else:
            self.y = map_height - self.height
