import pygame
from GameSetup.gameplay import difficulty, bounce, gameSave, game
from GameSetup import *


# make font object
pygame.init()
font = pygame.font.SysFont(None, 30)
def menu(message):
    # blank screen
    window.fill((255,255,255))
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

        # move to next screen if space bar is pressed
        keysPressed = pygame.key.get_pressed()
        if keysPressed[pygame.K_SPACE]:
            game()

        # display cpu difficulty and lifetime stats
        import GameSetup.gameplay
        displayText(f"Level: {difficulty(read=True)}", font, (0,73,140), 0, 50)
        displayText(f"Total Bounces: {bounce(read= True)}", font, (216, 2, 140), 0, 30)
        displayText("Press Space To Start New Round", font, (50, 73, 0), 0, -30)
        displayText(message, font, (0, 73, 140), 0, 0)



# function for displaying text because pygame does not have built in functionality
def displayText(text, font, color, x, y):
    # render text into image
    imageOfText = font.render(text, False, color)
    # get the size of that image
    imageHeight = imageOfText.get_rect().bottom
    imageWidth = imageOfText.get_rect().right
    # put it on the screen
    window.blit(imageOfText, (centerx - imageWidth/2 +x, centery- imageHeight/2 -y))

