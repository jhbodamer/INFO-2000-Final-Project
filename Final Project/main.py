# simple pong game
import pygame

# create classes ill come back to

#set the size of the window and make screen object
w = 400
h = 400
window = pygame.display.set_mode((w,h))

#pygame setup stuff
clock = pygame.time.Clock()
# fill window with white color
window.fill((255,255,255), (0,0,w,h))


class Ball:
    def __init__(self, size, speed):
        self.radius = size
        self.speed = speed


class Paddle:
    def __init__(self, length, speed):
        self.length = length
        self.speed = speed

# looking at examples online, pygame needs a loop to run
while True:
    # this sets how fast the game will run
    clock.tick(100)