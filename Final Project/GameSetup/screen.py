import pygame
from GameSetup.gamesetup import startingDifficulty, windowSize
# set the size of the window and make display object
if windowSize == "S":
    w = 400
    h = 400
elif windowSize == "M":
    w = 700
    h = 700
elif windowSize == 'L':
    w = 1000
    h = 1000
else:
    raise ValueError

window = pygame.display.set_mode((w,h))

# make a center as this game is based on a circle
centerx = w/2
centery = h/2

# pygame setup stuff
clock = pygame.time.Clock()

# fill window with white color
window.fill((255, 255, 255))

# set window caption
pygame.display.set_caption("INFO 2000 Final Project")