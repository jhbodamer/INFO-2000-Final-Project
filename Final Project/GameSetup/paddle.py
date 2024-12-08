import random

import pygame
from GameSetup.screen import window, centerx, centery
import math
from random import randrange, seed

class Paddle:
    def __init__(self, length, speed, radius, angle):
        self.length = length
        self.speed = speed

        self.radius = radius
        self.angle = angle
        self.previousAngle = angle


    # make a class to draw paddle
    def drawAngle(self, shadow=False, cpu = False):
        # doing some math to draw a line representing the paddle given the angle
        # this is for drawing over where the paddle just was
        if shadow:
            angleForCalculations = self.previousAngle + math.pi / 2
            color = (255,255,255)
            self.lineStart = (centerx + math.cos(self.previousAngle) * self.radius + math.cos(angleForCalculations) * self.length,
                         centery + math.sin(self.previousAngle) * self.radius + math.sin(angleForCalculations) * self.length)
            self.lineEnd = (centerx + math.cos(self.previousAngle) * self.radius - math.cos(angleForCalculations) * self.length,
                       centery + math.sin(self.previousAngle) * self.radius - math.sin(angleForCalculations) * self.length)
        # this is for drawing where the paddle currently is
        else:
            color = (255, 150 , 0)
            if cpu:
                color = (0 ,0, 0)
            angleForCalculations = self.angle + math.pi / 2
            self.lineStart = (centerx + math.cos(self.angle) * self.radius + math.cos(angleForCalculations) * self.length,
                         centery + math.sin(self.angle) * self.radius + math.sin(angleForCalculations) * self.length)
            self.lineEnd = (centerx + math.cos(self.angle) * self.radius - math.cos(angleForCalculations) * self.length,
                       centery + math.sin(self.angle) * self.radius - math.sin(angleForCalculations) * self.length)
        #once the start and end of the line had been defined, draw it
        pygame.draw.line(window, color, self.lineStart , self.lineEnd, width= 3)

    # this updates the paddle based on the speed attrivbute and key pressed
    def update(self):
        self.previousAngle = self.angle
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_LEFT]:
            self.drawAngle(True)
            self.angle -= math.pi * 0.01 * self.speed
        if keysPressed[pygame.K_RIGHT]:
            self.angle += math.pi * 0.01 * self.speed
            self.drawAngle(True)
        self.drawAngle(False)



# making a class for just the cpu paddle using inheritance from the paddle class above
class CpuPaddle(Paddle):
    # searched it up and you need this to inherit init class and add to it
    def __init__(self, length, speed, radius, angle, randomness):
        super().__init__(length, speed, radius, angle)
        # this parameter will add unpredictable movements to the cpu paddle
        self.noise = randomness
        # self.color = color

    # add small randomized movement to the cpu
    def update(self, ball):
        # store where paddle is to draw over it
        self.previousAngle = self.angle
        # move position randomly
        self.angle = float(self.angle)+randrange(-self.noise+1, self.noise)*0.01
        # convert angles to all positive
        correctedBallAngle = (ball.angleWillCollide + math.pi)%(2*math.pi)
        correctedPadAngle = (self.angle + math.pi)%(2*math.pi)

        # move the paddle to where the ball will hit
        if 0 < (correctedBallAngle - correctedPadAngle) < math.pi and ball.lastPaddle == "player":
            self.angle += 2*self.speed
        elif ball.lastPaddle == 'player':
            self.angle -= 2*self.speed


        # if correctedBallAngle - correctedPadAngle < 0 and self.angle > -math.pi and ball.lastPaddle == "player":
        #     self.angle -= self.speed
        # else:
        #     self.angle += self.speed
        # draw the paddle
        self.drawAngle(True)
        self.drawAngle(False, cpu=True)
        # print(self.angle)