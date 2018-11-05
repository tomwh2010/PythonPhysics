##############################################################################
#Description
#moving object at angle
#i.e. change y and x
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
#ball color
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

#Frames pr second
FPS=40

#window size
WIDTH=600
HEIGHT=600

#ballsize
BALLSIZE=10

#how close to the edge before bouncing
BOUNCEDISTANCE=8

#delta x,y
DELTA_X=6
DELTA_Y=4

##############################################################################
#variables
##############################################################################
#initial delta and start
delta_y=DELTA_Y
delta_x=DELTA_X
myball=[10, 100]

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
pygame.display.set_caption('Framework')

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

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, myball, BALLSIZE, FILLSTYLE)

    #update position
    myball[0]+=delta_x
    myball[1]+=delta_y

    #calcualte new delta if bouncing
    if myball[1]>=(HEIGHT-BOUNCEDISTANCE):
        delta_y=-DELTA_Y
    if myball[1]<=BOUNCEDISTANCE:
        delta_y=DELTA_Y
    if myball[0]>=(WIDTH-BOUNCEDISTANCE):
        delta_x=-DELTA_X
    if myball[0]<=BOUNCEDISTANCE:
        delta_x=DELTA_X

    #update display
    pygame.display.flip()
