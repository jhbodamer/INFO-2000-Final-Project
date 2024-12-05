# import module with all the classes and functions
from GameSetup import *

# make objects
playerPaddle = Paddle(20, 1 , 100, math.pi/2)
cpuPaddle = CpuPaddle(30, 0, 200, 3*math.pi/2, randomness= 4)
ball = Ball(5,0)
count = 0

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
        count += 1

        print (count)
    #end game if the ball goes out of game area with different exit codes for debugging
    if abs(ball.position[0]-centerx) > abs(cpuPaddle.radius) + 10:
        exit(1)
    if abs(ball.position[1]-centery) > abs(cpuPaddle.radius) + 10:
        exit(2)


