import pygame

# set the size of the window and make display object
w = 400
h = 400
window = pygame.display.set_mode((w,h))

# make a center as this game is based on a circle
centerx = w/2
centery = h/2

# pygame setup stuff
clock = pygame.time.Clock()

# fill window with white color
window.fill((255, 255, 255))