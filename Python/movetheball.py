##############################################################################
#Description
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors

##############################################################################
#constants
##############################################################################
#color of the ball
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

#Frames pr second
FPS=40

#window size
WIDTH=800
HEIGHT=500

##############################################################################
#variables
##############################################################################

##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Move a ball')

# creates a clock
clock=pygame.time.Clock()

#initial location of the ball; center
myball=[WIDTH//2, HEIGHT//2]

##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill(twhcolors.SILVER)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if any key is pressed
        elif event.type==pygame.KEYDOWN:
            # if the 'up' key is pressed
            if event.key==pygame.K_UP:
                # moves the blue rectangle 1 pixel up
                myball[1]-=10

            # if the 'down' key is pressed
            elif event.key==pygame.K_DOWN:
                # moves the blue rectangle 1 pixel down
                myball[1]+=10

            # if the 'left' key is pressed
            elif event.key==pygame.K_LEFT:
                # moves the blue rectangle 1 pixel to the left
                myball[0]-=10

            # if the 'right' key is pressed
            elif event.key==pygame.K_RIGHT:
                # moves the blue rectangle 1 pixel to the right
                myball[0]+=10

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, myball, 10, FILLSTYLE)

    #update display
    pygame.display.flip()
