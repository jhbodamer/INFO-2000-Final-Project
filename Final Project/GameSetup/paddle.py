import pygame
from GameSetup.screen import window, centerx, centery
import math
class Paddle:
    def __init__(self, length, speed, radius, angle):
        self.length = length
        self.speed = speed

        self.radius = radius
        self.angle = angle
        self.previousAngle = angle


    # make a class to draw paddle
    def drawAngle(self, previous=False):
        # doing some math to draw a line representing the paddle given the angle

        if previous:
            angleForCalculations = self.previousAngle + math.pi / 2
            color = (255,255,255)
            self.lineStart = (centerx + math.cos(self.previousAngle) * self.radius + math.cos(angleForCalculations) * self.length,
                         centery + math.sin(self.previousAngle) * self.radius + math.sin(angleForCalculations) * self.length)
            self.lineEnd = (centerx + math.cos(self.previousAngle) * self.radius - math.cos(angleForCalculations) * self.length,
                       centery + math.sin(self.previousAngle) * self.radius - math.sin(angleForCalculations) * self.length)
        else:
            color = (0,0,0)
            angleForCalculations = self.angle + math.pi / 2
            self.lineStart = (centerx + math.cos(self.angle) * self.radius + math.cos(angleForCalculations) * self.length,
                         centery + math.sin(self.angle) * self.radius + math.sin(angleForCalculations) * self.length)
            self.lineEnd = (centerx + math.cos(self.angle) * self.radius - math.cos(angleForCalculations) * self.length,
                       centery + math.sin(self.angle) * self.radius - math.sin(angleForCalculations) * self.length)
        pygame.draw.line(window, color, self.lineStart , self.lineEnd, width= 3)

        # pygame.draw.arc(window, (255, 255, 255), pygame.Rect(centerx - self.radius-1, centery - self.radius-1, self.radius * 2+2,
        #                                                self.radius * 2+2), self.angle + self.length, self.angle, width = 5)
        # # using the draw arc function in python
        # pygame.draw.arc(window, (0, 0, 0), pygame.Rect(centerx-self.radius, centery-self.radius, self.radius*2,
        # self.radius*2), self.angle, self.angle+self.length, 3)
    def update(self):
        self.previousAngle = self.angle
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_LEFT]:
            self.drawAngle(True)
            self.angle -= math.pi * 0.01
        if keysPressed[pygame.K_RIGHT]:
            self.angle += math.pi * 0.01
            self.drawAngle(True)
        self.drawAngle(False)