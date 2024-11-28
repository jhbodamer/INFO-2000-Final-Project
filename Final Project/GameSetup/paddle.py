import pygame
import math
from GameSetup.screen import window, centerx, centery
class Paddle:
    def __init__(self, length, speed, radius, angle):
        self.length = length
        self.speed = speed

        self.radius = radius
        self.angle = angle

    # make a class to draw paddle
    def draw(self):
        pygame.draw.arc(window, (255, 255, 255), pygame.Rect(centerx - self.radius, centery - self.radius, self.radius * 2,
                                                       self.radius * 2), self.angle + self.length, self.angle, width = 3)
        # using the draw arc function in python
        pygame.draw.arc(window, (0, 0, 0), pygame.Rect(centerx-self.radius, centery-self.radius, self.radius*2,
        self.radius*2), self.angle, self.angle+self.length)
