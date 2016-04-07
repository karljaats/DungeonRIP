import pygame
import shared_vars
from src import Camera, Map, Monster, Player


class Game:
    def __init__(self):
        self.images = {"wall": pygame.image.load("pics/wall.png").convert(),
                       "floor": pygame.image.load("pics/floor.png").convert(),
                       "player": pygame.image.load("pics/player.png").convert(),
                       "stair_up": pygame.image.load("pics/stair_up.png").convert(),
                       "stair_down": pygame.image.load("pics/stair_down.png").convert(),
                       "black": pygame.image.load("pics/black.png").convert(),
                       "monster": pygame.image.load("pics/monster.png").convert()}

        font = pygame.font.Font(None, 28)
        self.camera = Camera(shared_vars.screen_w, shared_vars.screen_h, shared_vars.tile_size, font)

        self.map = Map(self.images)
        player_pos = self.map.generate_map()

        self.player = Player(player_pos[0], player_pos[1], self.images)
        self.monsters = []

    def on_event(self, event):
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
            elif event.key == pygame.K_LESS:
                if self.map.map[self.player.x][self.player.y] == "stair_up":
                    self.map.level -= 1
                    self.monsters = []
                    player_pos = self.map.generate_map()
                    self.player.x = player_pos[0]
                    self.player.y = player_pos[1]
                elif self.map.map[self.player.x][self.player.y] == "stair_down":
                    self.map.level += 1
                    self.monsters = []
                    player_pos = self.map.generate_map()
                    self.player.x = player_pos[0]
                    self.player.y = player_pos[1]

    def update(self):
        while len(self.monsters) < 10:
            monster_pos = self.map.generate_monster()
            self.monsters.append(Monster(monster_pos[0], monster_pos[1], self.images))

    def draw(self, screen):
        self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
        self.camera.draw(screen, self.map, self.monsters, self.player)
