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
#line thickness
LINESTYLE=2

#Frames pr second
FPS=20

#window size
WIDTH=600
HEIGHT=600

#delta x, y for each update
DELTA=10

##############################################################################
#variables
##############################################################################
#initial start, end point for line
x_start=0
y_start=300
x_stop=300
y_stop=0

#initial delta for start, stop
dx_start=0
dy_start=-DELTA
dx_stop=DELTA
dy_stop=0

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
    pygame.draw.line(screen, twhcolors.getColor(), (x_start, y_start), (x_stop, y_stop), LINESTYLE)

    #update color
    twhcolors.cyclecolor()

    #change deltas if hitting one of the four corners
    if x_start==0 and y_start==0:
        dx_start=DELTA
        dy_start=0
        dx_stop=0
        dy_stop=DELTA

    if x_start==HEIGHT and y_start==0:
        dx_start=0
        dy_start=DELTA
        dx_stop=-DELTA
        dy_stop=0

    if x_start==HEIGHT and y_start==HEIGHT:
        dx_start=-DELTA
        dy_start=0
        dx_stop=0
        dy_stop=-DELTA

    if x_start==0 and y_start==HEIGHT:
        dx_start=0
        dy_start=-DELTA
        dx_stop=DELTA
        dy_stop=0

    #update ned start, end points
    x_start+=dx_start
    y_start+=dy_start
    x_stop+=dx_stop
    y_stop+=dy_stop

    #update display
    pygame.display.flip()
