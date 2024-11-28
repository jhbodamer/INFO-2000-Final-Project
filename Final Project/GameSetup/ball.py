# simple 360 pong game
import pygame
from GameSetup.screen import centerx, centery, window
import math

class Ball:
    def __init__(self, size, speed, pos=(centerx, centery)):
        self.radius = size
        self.speed = speed
        self.position = pos
        self.previousPos = pos
    # draw function that also tracks the previous position and draws over it
    def draw(self):
        pygame.draw.circle(window, (0, 0, 255), self.position, self.radius )

