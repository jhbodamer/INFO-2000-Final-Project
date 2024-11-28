# looking at examples online, pygame needs a loop to run
from GameSetup import *


test = Paddle(7, 0 , 100, 0)
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
    test.update()

    ball.draw()