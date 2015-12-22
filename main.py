import pygame
from player import Player
from map import Map
from camera import Camera

pygame.init()

screen_w, screen_h = 40, 30
tile_size = 20

screen = pygame.display.set_mode((screen_w*tile_size, screen_h*tile_size))
pygame.display.set_caption("Dungeon")

clock = pygame.time.Clock()

images = {"wall": pygame.image.load("pics/wall.png").convert(),
          "floor": pygame.image.load("pics/floor.png").convert(),
          "player": pygame.image.load("pics/player.png").convert()}

player = Player(50, 50, images)

map = Map(images)
map.generate_map(100, 100)

camera = Camera(30, 35, screen, tile_size)

characters = {"player": player}

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                if player.move(-1, 1, map):
                    camera.move(-1, 1, map.width, map.height)
            elif event.key == pygame.K_DOWN or event.key == pygame.K_KP2:
                if player.move(0, 1, map):
                    camera.move(0, 1, map.width, map.height)
            elif event.key == pygame.K_KP3:
                if player.move(1, 1, map):
                    camera.move(1, 1, map.width, map.height)
            elif event.key == pygame.K_LEFT or event.key == pygame.K_KP4:
                if player.move(-1, 0, map):
                    camera.move(-1, 0, map.width, map.height)
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_KP6:
                if player.move(1, 0, map):
                    camera.move(1, 0, map.width, map.height)
            elif event.key == pygame.K_KP7:
                if player.move(-1, -1, map):
                    camera.move(-1, -1, map.width, map.height)
            elif event.key == pygame.K_UP or event.key == pygame.K_KP8:
                if player.move(0, -1, map):
                    camera.move(0, -1, map.width, map.height)
            elif event.key == pygame.K_KP9:
                if player.move(1, -1, map):
                    camera.move(1, -1, map.width, map.height)

    screen.fill((255, 255, 255))
    screen.blit(camera.draw(map, characters), (0, 0))
    clock.tick()
    pygame.display.flip()

pygame.quit()
