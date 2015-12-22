import pygame
from player import Player
from map import Map


class Game:
    def __init__(self, images, camera):
        self.images = images
        self.camera = camera

        self.map = Map(images)
        self.map.generate_map(100, 100)

        self.player = Player(50, 50, images)
        self.characters = {"player": self.player}

        self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                if self.player.move(-1, 1, self.map):  # if players move was successful
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                if self.player.move(0, 1, self.map):
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
            elif event.key == pygame.K_KP3:
                if self.player.move(1, 1, self.map):
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                if self.player.move(-1, 0, self.map):
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                if self.player.move(1, 0, self.map):
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
            elif event.key == pygame.K_KP7:
                if self.player.move(-1, -1, self.map):
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
            elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                if self.player.move(0, -1, self.map):
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
            elif event.key == pygame.K_KP9:
                if self.player.move(1, -1, self.map):
                    self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)

    def draw(self):
        return self.camera.draw(self.map, self.characters)
