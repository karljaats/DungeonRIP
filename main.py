import pygame
from in_game import Game
from camera import Camera

pygame.init()

screen_w, screen_h = 40, 30  # in tiles
tile_size = 20  # square, in pixels

screen = pygame.display.set_mode((screen_w*tile_size, screen_h*tile_size))
pygame.display.set_caption("Dungeon")

clock = pygame.time.Clock()

images = {"wall": pygame.image.load("pics/wall.png").convert(),
          "floor": pygame.image.load("pics/floor.png").convert(),
          "player": pygame.image.load("pics/player.png").convert()}

camera = Camera(screen_w, screen_h, tile_size)

game = Game(images, camera)

state = game

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        else:
            state.handle_event(event)

    screen.fill((0, 0, 0))
    screen.blit(state.draw(), (0, 0))
    clock.tick()
    pygame.display.flip()

pygame.quit()
