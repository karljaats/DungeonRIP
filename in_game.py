import pygame
import shared_vars
import random
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

        self.big_font = pygame.font.Font(None, 50)

        self.map = Map(self.images)
        player_pos = self.map.generate_map()

        self.player = Player(player_pos[0], player_pos[1], self.images)
        self.monsters = []

        self.dead = False

        self.process_turn()

    def on_event(self, event):
        """
        State'i põhiste eventide käsitlemine
        :param event: praegune event
        :return: None
        """
        if event.type == pygame.KEYDOWN:
            if not self.dead:
                if event.key == pygame.K_KP1:
                    self.player.move(-1, 1, self.map, self.monsters)
                elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                    self.player.move(0, 1, self.map, self.monsters)
                elif event.key == pygame.K_KP3:
                    self.player.move(1, 1, self.map, self.monsters)
                elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                    self.player.move(-1, 0, self.map, self.monsters)
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                    self.player.move(1, 0, self.map, self.monsters)
                elif event.key == pygame.K_KP7:
                    self.player.move(-1, -1, self.map, self.monsters)
                elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                    self.player.move(0, -1, self.map, self.monsters)
                elif event.key == pygame.K_KP9:
                    self.player.move(1, -1, self.map, self.monsters)
                elif event.key == pygame.K_KP5:
                    pass  # oota üks käik
                elif event.key == pygame.K_LESS:
                    if self.map.map[self.player.x][self.player.y] == "stair_up":
                        self.map.level -= 1
                    elif self.map.map[self.player.x][self.player.y] == "stair_down":
                        self.map.level += 1
                    self.monsters = []
                    player_pos = self.map.generate_map()
                    self.player.x = player_pos[0]
                    self.player.y = player_pos[1]
                self.process_turn()
            elif event.key == pygame.K_SPACE:
                shared_vars.restart = True

    # kutsutakse iga frame
    def update(self):
        """
        Ei tee praegu midagi, teistes stateides teeks
        :return: None
        """
        pass

    def draw(self, screen):
        """
        joonistamine
        :param screen: aken
        :return: None
        """
        self.camera.center(self.map.width, self.map.height, self.player.x, self.player.y)
        self.camera.draw(screen, self.map, self.monsters, self.player)
        if self.dead:
            screen.blit(self.big_font.render("You died!", True, (255, 255, 255)), (300, 275))

    def process_turn(self):
        """
        Vaenlaste käik
        :return: None
        """
        dead_monsters = []
        for i in range(len(self.monsters)):
            monster = self.monsters[i]
            if monster.current_health <= 0:
                dead_monsters.append(i)
            else:
                monster.update(self.map, self.player, self.monsters)

        for i in dead_monsters:
            self.monsters.pop(i)

        if len(self.monsters) > 0:
            while len(self.monsters) < 10:
                monster_pos = self.map.generate_monster(self.camera)
                self.monsters.append(Monster(monster_pos[0], monster_pos[1], self.images))
        else:
            # kui esimest korda genereerida, siis kaamera asukohta mitte vaadata
            while len(self.monsters) < 10:
                monster_pos = [0, 0]
                while True:
                    monster_pos = [random.randint(0, self.map.width-1), random.randint(0, self.map.height-1)]
                    if self.map.map[monster_pos[0]][monster_pos[1]] == "floor":
                        break
                self.monsters.append(Monster(monster_pos[0], monster_pos[1], self.images))

        self.player.update()
        if self.player.current_health < 0:
            self.dead = True
