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
        self.angleWillCollide = 0

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
        # check collision with both paddles and update velocity if necessary
        # check if the ball is hitting any paddles
        for i in tupleOfPaddles:
            if self.checkCollision(i):
            # change the velocity based on the principle angle of incidence = angle of reflection
                # calculate angle that the ball is travelling at
                oldAngleOfBall = math.atan2(self.velocity[1],self.velocity[0])
                # change velocity
                angleOfPaddle = i.angle - math.pi / 2
                newAngleOfBall = 2*angleOfPaddle - oldAngleOfBall
                self.velocity = (1*math.cos(newAngleOfBall), 1*math.sin(newAngleOfBall))
                # move the ball until it is not colliding anymore
                self.previousPos = self.position
                self.draw(True)
                while self.checkCollision(i):
                    self.position = numpy.add(self.position, (math.cos(newAngleOfBall)*1,math.sin(newAngleOfBall)*1))
                # use function below to recalculate where the ball will go so the cpu has an idea of where to go
                self.calculateangleforcpu(tupleOfPaddles[1])
                print('Angle ball will collide in degrees: ', self.angleWillCollide / math.pi / 2 * 360)
                print(tupleOfPaddles[0].angle / math.pi / 2 * 360)



        # add velocity and postion vectors
        self.position = numpy.add(self.position, self.velocity)
        # draw new location
        self.draw(False)


    # calculate where the ball will hit given its velocity and time so the cpu knows where to move
    # dont know a bettr way to do this so i will just simulate using for loop
    def calculateangleforcpu(self, paddle):
        simPosition = self.position
        while simPosition[0] ** 2 + simPosition[1] ** 2 < paddle.radius**2:
            numpy.add(simPosition, self.velocity)
        self.angleWillCollide = math.atan2(simPosition[1]-centery, simPosition[0]-centerx)


    def checkCollision(self, paddleToCheck):
        listOfLinePoints = list()
        #make a list of 10 points on the paddle
        for i in range(10):
            listOfLinePoints.append((paddleToCheck.lineStart[0]+i*(paddleToCheck.lineEnd[0]-paddleToCheck.lineStart[0])/10,
                                    paddleToCheck.lineStart[1] + i * (paddleToCheck.lineEnd[1] - paddleToCheck.lineStart[1]) / 10))
        # for each point on the line, check if the distance to the center of the ball is less than the radius of the ball
        for i in listOfLinePoints:
            if (((i[0]-self.position[0])**2+(i[1]-self.position[1])**2)**0.5) < self.radius+2:
                return True


