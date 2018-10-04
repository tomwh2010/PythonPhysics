##############################################################################
#Description
#moving object horizontally
#i.e. change x
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
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

FPS=40 #Frames pr second

#window size
WIDTH=600
HEIGHT=600

BALLSIZE=10
BOUNCEDISTANCE=8
DELTA=5

##############################################################################
#variables
##############################################################################
delta_x=DELTA
myball=[BOUNCEDISTANCE, HEIGHT//2]

##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

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
    if myball[0]>=(WIDTH-BOUNCEDISTANCE):
        delta_x=-DELTA
    if myball[0]<=BOUNCEDISTANCE:
        delta_x=DELTA

    #update display
    pygame.display.flip()
