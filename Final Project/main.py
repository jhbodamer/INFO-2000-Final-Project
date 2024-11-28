# simple pong game
import pygame
import math

# create classes ill come back to

#set the size of the window and make screen object
w = 400
h = 400
window = pygame.display.set_mode((w,h))
#make a center as this game is based on a circle
centerx = w/2
centery = h/2
#pygame setup stuff
clock = pygame.time.Clock()
# fill window with white color
window.fill((255,255,255))


class Ball:
    def __init__(self, size, speed):
        self.radius = size
        self.speed = speed


class Paddle:
    def __init__(self, length, speed, radius, angle):
        self.length = length
        self.speed = speed

        self.radius = radius
        self.angle = angle

    # make a class to draw paddle
    def draw(self):
        # using the draw arc function in python
        pygame.draw.arc(window, (0, 0, 0), pygame.Rect(centerx-self.radius, centery-self.radius, self.radius*2,
        self.radius*2), self.angle, self.angle+self.length)
# looking at examples online, pygame needs a loop to run
while True:
    # this sets how fast the game will run
    clock.tick(100)
    #update screen
    pygame.display.flip()
    #need this to prevent crashing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    #create test paddle obj
    test = Paddle(math.pi, 0 , 100, 0)
    test.draw()
    pygame.draw.circle(window, (0,0,0), (centerx,centery), 5)