##############################################################################
#Description
#moving thru a galaxy  full of stars
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors
import random

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
CENTERX=WIDTH//2
CENTERY=HEIGHT//2

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
animation=True
stars=[]

##############################################################################
#functions
##############################################################################
def generatestars0():
    N=1000
    for i in range(N):
        x=random.randint(0, WIDTH)-CENTERX
        y=random.randint(0, HEIGHT)-CENTERY
        r=(x**2+y**2)**0.5
        theta=1
        star=[x, y]
        stars.append(star)

def drawstars():
    for i in stars:
        pygame.draw.circle(screen, twhcolors.WHITE, (i[0], i[1]), 3, FILLSTYLE)

def fly():
    #calculate theta for each star
    #move outward
    x=1
    """
    x = r × cos( θ )
    y = r × sin( θ )
    """
##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

# creates a clock
clock=pygame.time.Clock()

generatestars0()

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
    if animation:
        #draw background color to blank the screen
        screen.fill(twhcolors.BLACK)

        drawstars()

    #update display
    pygame.display.flip()
