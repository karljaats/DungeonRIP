import pygame
from player import Player
from map import Map


class Game:
    def __init__(self, images, camera):
        self.images = images
        self.camera = camera

        self.map = Map(images)
        self.map.generate_map()

        self.player = Player(50, 50, images)
        self.characters = {"player": self.player}

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                self.player.move(-1, 1, self.map)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                self.player.move(0, 1, self.map)
            elif event.key == pygame.K_KP3:
                self.player.move(1, 1, self.map)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                self.player.move(-1, 0, self.map)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                self.player.move(1, 0, self.map)
            elif event.key == pygame.K_KP7:
                self.player.move(-1, -1, self.map)
            elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                self.player.move(0, -1, self.map)
            elif event.key == pygame.K_KP9:
                self.player.move(1, -1, self.map)

    def draw(self):
        self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
        return self.camera.draw(self.map, self.characters)
