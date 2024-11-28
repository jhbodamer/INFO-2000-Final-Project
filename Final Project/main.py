# import module with all the classes and functions
from GameSetup import *

# make objects
playerPaddle = Paddle(7, 1 , 100, math.pi/2)
cpuPaddle = Paddle(7, 0, 130, 3*math.pi/2)
ball = Ball(5,0)

# looking at examples online, pygame needs a loop to run
while True:
    # this sets how fast the game will run
    screen.clock.tick(100)
    #update screen
    pygame.display.flip()
    #need this to prevent crashing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit(0)

    # update paddle
    playerPaddle.update()
    cpuPaddle.update()
    # update ball postion and print if it is colliding with player paddle
    ball.update((playerPaddle, cpuPaddle))
    if ball.checkCollision(playerPaddle):
        print('collided')