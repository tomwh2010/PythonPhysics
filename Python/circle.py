##############################################################################
#Description
#Ball moves in a circle
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors

##############################################################################
#constants
##############################################################################
#Frames pr second
FPS=4

#window size
WIDTH=400
HEIGHT=400

#center x,y and radius
STARTX=WIDTH//2
STARTY=HEIGHT//2
RADIUS=190

#change to negative number for counterclockwise
DELTA=2

##############################################################################
#variables
##############################################################################
#initial angle
angle=0

#initial x, y for ball
ballx=STARTY
bally=STARTY-RADIUS

##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Clock')

# creates a clock
clock=pygame.time.Clock()

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

    #paint ball
    pygame.draw.circle(screen, twhcolors.BLACK, (ballx, bally), 5, 0)

    #update angle
    angle+=DELTA
    theta=radians(angle)

    #calculate x,y for ball
    ballx=STARTX+int(RADIUS*sin(theta))
    bally=STARTY-int(RADIUS*cos(theta))

    #update display
    pygame.display.flip()
