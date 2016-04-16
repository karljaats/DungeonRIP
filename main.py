import pygame
import shared_vars
from in_game import Game

pygame.init()

screen = pygame.display.set_mode((shared_vars.screen_w * shared_vars.tile_size, shared_vars.screen_h * shared_vars.tile_size))
pygame.display.set_caption("Dungeon")

clock = pygame.time.Clock()

shared_vars.game = Game()

shared_vars.state = shared_vars.game

while not shared_vars.quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shared_vars.quit_game = True
        else:
            shared_vars.state.on_event(event)

    if shared_vars.restart:
        shared_vars.game = Game()
        shared_vars.state = shared_vars.game
        shared_vars.restart = False

    shared_vars.state.update()
    shared_vars.state.draw(screen)

    clock.tick()
    pygame.display.flip()

pygame.quit()
