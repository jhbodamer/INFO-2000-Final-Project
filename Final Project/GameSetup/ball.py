# simple 360 pong game
import pygame
from GameSetup.screen import centerx, centery, window
from .gameplay import bounce
import numpy
import math


#class for ball that bounces
class Ball:
    def __init__(self, size, speed, pos=(centerx, centery)):
        self.radius = size
        self.speed = speed
        self.position = pos
        self.previousPos = pos
        self.velocity = (0, speed)
        self.angleWillCollide = 0
        self.color = (0, 0, 255)

        # variable to track which paddle last hit the ball
        self.lastPaddle = "computer"
    # draw function that draws
    #either current position or over previous
    #depending on paramerter
    def draw(self, shadow = False):
        if shadow:
            pygame.draw.circle(window, (255, 255, 255), self.previousPos, self.radius )
        else:
            pygame.draw.circle(window, (self.color), self.position, self.radius)


    def update(self, tupleOfPaddles):
        # store previous position
        global lastPaddle
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
                magnitudeOfVelo = math.sqrt(self.velocity[0]**2+self.velocity[1]**2)
                self.velocity = (magnitudeOfVelo*math.cos(newAngleOfBall), magnitudeOfVelo*math.sin(newAngleOfBall))
                # move the ball until it is not colliding anymore
                self.previousPos = self.position
                self.draw(True)
                while self.checkCollision(i):
                    self.position = numpy.add(self.position, (math.cos(newAngleOfBall)*1,math.sin(newAngleOfBall)*1))
                # use function below to recalculate where the ball will go so the cpu has an idea of where to go
                self.calculateangleforcpu(tupleOfPaddles[1])
                # track who hit the ball last
                if i == tupleOfPaddles[0]:
                    self.lastPaddle = 'player'
                    self.color = (0, 255, 0)
                    bounce(False)
                else:
                    self.lastPaddle = "computer"
                    self.color = (255, 0, 0)
                # print(self.lastPaddle)



        # add velocity and postion vectors
        self.position = numpy.add(self.position, self.velocity)
        # draw new location
        self.draw(False)


    # calculate where the ball will hit given its velocity and time so the cpu knows where to move
    # dont know a bettr way to do this so i will just simulate using for loop
    def calculateangleforcpu(self, paddle):
        # make fake ball and add velocity til it hits the paddle's radius
        simPosition = self.position
        while math.sqrt((simPosition[0]-centerx)**2 + (simPosition[1]-centery)**2) < paddle.radius:
            simPosition = numpy.add(simPosition, self.velocity)
        # once the fake ball hits record its angle
        self.angleWillCollide = math.atan2(simPosition[1]-centery, simPosition[0]-centerx)
        # print(self.angleWillCollide)




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


