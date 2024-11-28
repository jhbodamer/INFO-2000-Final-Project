# simple 360 pong game
import pygame
from GameSetup.screen import centerx, centery, window
import numpy
import math

class Ball:
    def __init__(self, size, speed, pos=(centerx, centery), velocity = (0,1)):
        self.radius = size
        self.speed = speed
        self.position = pos
        self.previousPos = pos
        self.velocity = velocity
    # draw function that also tracks the previous position and draws over it

    def draw(self, shadow = False):
        if shadow:
            pygame.draw.circle(window, (255, 255, 255), self.previousPos, self.radius )
        else:
            pygame.draw.circle(window, (0, 0, 255), self.position, self.radius)

    def update(self):
        self.previousPos = self.position
        self.draw(True)
        self.position = numpy.add(self.position, self.velocity)
        self.draw(False)
