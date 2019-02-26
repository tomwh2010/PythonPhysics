##############################################################################
#Description
#push a box with extendable rods
# the further you push the faster it GOES
# if pushed off a 1 cell block then speed is 1
# if ball hangs by a pendulum then it will release upon hitting
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
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

FPS=40 #Frames pr second

#window size
WIDTH=600
HEIGHT=600

BALLSIZE=10
BOUNCEDISTANCE=8
DELTA_X=6
DELTA_Y=4

##############################################################################
#variables
##############################################################################
delta_y=DELTA_Y
delta_x=DELTA_X
myball=[10, 100]

##############################################################################
#functions
##############################################################################
def paintbar(nr, x0, y0, size, direction, extended):
    width=50+(size-1)*extended*50
    height=20
    if direction==1:
        width, height=height, width
    pygame.draw.rect(screen, twhcolors.YELLOW, (x0, y0, width, height), FILLSTYLE)
    #paint nr, size,


##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

# creates a clock
clock=pygame.time.Clock()

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


    #update position
    paintbar(1, 100, 50, 3, 0, 1)
    paintbar(1, 50, 250, 5, 1, 1)

    #update display
    pygame.display.flip()
