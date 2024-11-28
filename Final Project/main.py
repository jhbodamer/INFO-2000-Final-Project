# looking at examples online, pygame needs a loop to run
from GameSetup import *
import pygame
import math
test = Paddle(math.pi, 0 , 100, 0)
ball = Ball(5,0)
while True:
    # this sets how fast the game will run
    screen.clock.tick(100)
    #update screen
    pygame.display.flip()
    #need this to prevent crashing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    #create test paddle obj
    test.draw()
    keysPressed = pygame.key.get_pressed()
    if keysPressed[pygame.K_LEFT]:
        test.angle+= math.pi*0.01
    if keysPressed[pygame.K_RIGHT]:
        test.angle-= math.pi*0.01
    ball.draw()