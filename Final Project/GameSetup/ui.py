import pygame
from GameSetup import *
def menu():
    while True:
        # this sets how fast the game will run
        screen.clock.tick(100)
        # update screen
        pygame.display.flip()
        # need this to prevent crashing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_SPACE]:
            GameSetup.gameplay.game()