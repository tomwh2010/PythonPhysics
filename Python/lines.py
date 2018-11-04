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
LINESTYLE=2

FPS=20 #Frames pr second

#window size
WIDTH=600
HEIGHT=600

STEP=10

##############################################################################
#variables
##############################################################################
x1=0
y1=300
x2=300
y2=0
dx1=0
dy1=-STEP
dx2=STEP
dy2=0

##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lines')

#draw background color to blank the screen
screen.fill(twhcolors.BLACK)

# creates a clock
clock=pygame.time.Clock()

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

    #line(screen, color, coords1(x, y), coords2(x, y), fillstyle
    pygame.draw.line(screen, twhcolors.getColor(), (x1, y1), (x2, y2), LINESTYLE)

    #update steps
    twhcolors.cyclecolor()

    if x1==0 and y1==0:
        dx1=STEP
        dy1=0
        dx2=0
        dy2=STEP

    if x1==WIDTH and y1==0:
        dx1=0
        dy1=STEP
        dx2=-STEP
        dy2=0

    if x1==WIDTH and y1==HEIGHT:
        dx1=-STEP
        dy1=0
        dx2=0
        dy2=-STEP

    if x1==0 and y1==HEIGHT:
        dx1=0
        dy1=-STEP
        dx2=STEP
        dy2=0

    x1+=dx1
    y1+=dy1
    x2+=dx2
    y2+=dy2

    #update display
    pygame.display.flip()
