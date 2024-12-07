from GameSetup import *
import pygame
from GameSetup.screen import centerx,centery
from GameSetup.screen import window
import math


def readFile():
    # read player data file
    # make globals so other function can read them
    global bounces
    global roundsPlayed
    global cpuDifficulty
    # read stats from file
    playerFile = open("playerdata.txt", 'r')
    listOfStats = playerFile.readlines()
    print(listOfStats)
    bounces = int(listOfStats[0][21:25])
    roundsPlayed = int(listOfStats[1][15:18])
    cpuDifficulty = int(listOfStats[2][16:19])
    playerFile.close()
    return bounces, roundsPlayed, cpuDifficulty

readFile()

def game():
    window.fill((255,255,255))
    readFile()
    # read player data file
    # make globals so other function can read them
    # read stats from file
    playerFile = open("playerdata.txt", 'r')
    listOfStats = playerFile.readlines()
    print(listOfStats)
    bounces = int(listOfStats[0][21:25])
    roundsPlayed = int(listOfStats[1][15:18])
    cpuDifficulty = int(listOfStats[2][16:19])
    playerFile.close()



    # calculate the game settings based on the difficulty
    paddleWidth  = math.ceil(30 * (1/(cpuDifficulty)**0.4))

    # make objects based on the difficulty
    playerPaddle = GameSetup.paddle.Paddle(paddleWidth, 1, 100, math.pi / 2)
    cpuPaddle = GameSetup.paddle.CpuPaddle(10, 0.008, 150, -math.pi / 2, randomness=1)
    ball = GameSetup.ball.Ball(3, 1)

    # looking at examples online, pygame needs a loop to run
    while True:
        # this sets how fast the game will run
        screen.clock.tick(100)
        # update screen
        pygame.display.flip()
        # need this to prevent crashing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameSave()
                print("Thanks for playing, your stats are saved")
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
        if abs(ball.position[0]-centerx) > abs(cpuPaddle.radius) + 30 or abs(ball.position[1]-centery) > abs(cpuPaddle.radius) + 30:
            if ball.lastPaddle == "computer":
                message = "Try Again"
            else:
                message = "Good Job!"
            roundsPlayed += 1
            cpuDifficulty += 1
            gameSave()
            GameSetup.ui.menu(message)

def gameSave():
    playerFile = open("playerdata.txt", 'w')
    playerFile.write(f"Total player bounces: {bounces}  \n")
    playerFile.write(f"Rounds Played: {roundsPlayed} \n")
    playerFile.write(f"CPU Difficulty: {cpuDifficulty}   \n ")
    playerFile.close()

    # function for either reading number of times ball has hit player paddle or adding to it
def bounce(read = False):
    global bounces
    if read:
        return bounces
    else:
        try:
            bounces += 1
        except:
            readFile()
            bounces += 1




    # function for increasing or reading cpu difficuly
def difficulty(read = False):
    global cpuDifficulty
    if read:
        return cpuDifficulty
    else:
        try:
            cpuDifficulty += 1
        except:
            readFile()
            cpuDifficulty += 1
