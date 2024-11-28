# simple 360 pong game
import pygame
from GameSetup.screen import centerx, centery, window
import numpy
import math

#class for ball that bounces
class Ball:
    def __init__(self, size, speed, pos=(centerx, centery), velocity = (0,1)):
        self.radius = size
        self.speed = speed
        self.position = pos
        self.previousPos = pos
        self.velocity = velocity

    # draw function that draws
    #either current position or over previous
    #depending on paramerter
    def draw(self, shadow = False):
        if shadow:
            pygame.draw.circle(window, (255, 255, 255), self.previousPos, self.radius )
        else:
            pygame.draw.circle(window, (0, 0, 255), self.position, self.radius)


    def update(self, tupleOfPaddles):
        # store previous position
        self.previousPos = self.position
        # draw over current position
        self.draw(True)
        #add velocity and postion vectors
        self.position = numpy.add(self.position, self.velocity)
        # draw new location
        self.draw(False)
        # check collision with both paddles
        for i in tupleOfPaddles:
            self.checkCollision(i)


    def checkCollision(self, paddleToCheck):
        listOfLinePoints = list()
        #make a list of 10 points on the paddle
        for i in range(10):
            listOfLinePoints.append((paddleToCheck.lineStart[0]+i*(paddleToCheck.lineEnd[0]-paddleToCheck.lineStart[0])/10,
                                    paddleToCheck.lineStart[1] + i * (paddleToCheck.lineEnd[1] - paddleToCheck.lineStart[1]) / 10))
        # for each point on the line, check if the distance to the center of the ball is less than the radius of the ball
        for i in listOfLinePoints:
            if (((i[0]-self.position[0])**2+(i[1]-self.position[1])**2)**0.5) < self.radius:
                return True


