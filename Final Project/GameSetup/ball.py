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

    def update(self, tupleOfPaddles):
        self.previousPos = self.position
        self.draw(True)
        self.position = numpy.add(self.position, self.velocity)
        self.draw(False)
        self.checkCollision(tupleOfPaddles)


    def checkCollision(self, paddleToCheck):
        # make a list of 10 points on the outside of th ball
        # listOfPoints = list()
        # for i in range(10):
        #     listOfPoints[i] = i * math.pi / 10
        # for i in listOfPoints:
        #     listOfPoints[i] = numpy.add((math.cos(listOfPoints[i])*self.radius,
        #                                  math.sin(listOfPoints[i]) *self.radius),(self.position))
        listOfLinePoints = list()
        #make a list of 10 points on the paddle
        for i in range(10):
            listOfLinePoints.append((paddleToCheck.lineStart[0]+i*(paddleToCheck.lineEnd[0]-paddleToCheck.lineStart[0])/10,
                                    paddleToCheck.lineStart[1] + i * (paddleToCheck.lineEnd[1] - paddleToCheck.lineStart[1]) / 10))
        for i in listOfLinePoints:
            if (((i[0]-self.position[0])**2+(i[1]-self.position[1])**2)**0.5) < self.radius:
                return True


        # put 10 points on the outside of the ball and check if any of them are close enough
