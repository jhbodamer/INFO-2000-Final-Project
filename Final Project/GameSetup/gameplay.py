from GameSetup import *
def game():
    window.fill((255,255,255))
    # make objects
    playerPaddle = Paddle(20, 1, 100, math.pi / 2)
    cpuPaddle = CpuPaddle(10, 0.008, 150, -math.pi / 2, randomness=6)
    ball = Ball(3, 0)
    count = 0
    # looking at examples online, pygame needs a loop to run
    while True:
        # this sets how fast the game will run
        screen.clock.tick(100)
        # update screen
        pygame.display.flip()
        # need this to prevent crashing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)

        # update paddle
        playerPaddle.update()
        # update cpu paddle (ball parameter is so it knows where to go)
        cpuPaddle.update(ball)
        # update ball
        ball.update((playerPaddle, cpuPaddle))

        # keep track of how many times the ball hits
        if ball.checkCollision(playerPaddle):
        # print('collided')
            pass

        # end game if the ball goes out of game area with different exit codes for debugging
        if abs(ball.position[0]-centerx) > abs(cpuPaddle.radius) + 30:
            #exit(1)
            ui.menu()
        if abs(ball.position[1]-centery) > abs(cpuPaddle.radius) + 30:
            #exit(2)
            ui.menu()
