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
FPS=4 #Frames pr second

#window size
WIDTH=400
HEIGHT=400

#center x,y and radius
STARTX=WIDTH//2
STARTY=HEIGHT//2

RADIUS=190

#change to negative number for counterclockwise
DELTA=5

##############################################################################
#variables
##############################################################################
angle=0
stopx=STARTY
stopy=STARTY-RADIUS

##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

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

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #paint ball
    pygame.draw.circle(screen, twhcolors.BLACK, (stopx, stopy), 5, 0)

    #update angle
    angle+=DELTA
    theta=radians(angle)

    #calculate stopx, stopy
    stopx=STARTX+int(RADIUS*sin(theta))
    stopy=STARTY-int(RADIUS*cos(theta))

    #update display
    pygame.display.flip()
