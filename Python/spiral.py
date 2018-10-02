##############################################################################
#Description
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
LINESTYLE=2

FPS=50 #Frames pr second

#window size
WIDTH=600
HEIGHT=600
CENTERX=WIDTH//2
CENTERY=HEIGHT//2

##############################################################################
#variables
##############################################################################
x1=0
y1=0
x2=0
y2=0
angle=0.0
length=0.1

#change these two to change the spiral size
deltalength=0.1
deltaangle=6.0

##############################################################################
#functions
##############################################################################

##############################################################################
#functions
##############################################################################
def reset():
    global x1, y1, x2, y2, angle, length
    x1=CENTERX
    y1=CENTERY
    x2=CENTERX
    y2=CENTERY
    angle=0
    length=1

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lines')

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

# creates a clock
clock=pygame.time.Clock()

#reset the variables
reset()

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

    #update coords
    angle+=deltaangle
    length+=deltalength
    if angle==360:
        angle=0
    theta=radians(angle)
    x1=x2
    y1=y2
    x2=x1+int(length*sin(theta))
    y2=y1-int(length*cos(theta))

    #if reached the edge then reset coords and choose new color
    if x1<0 or x1>WIDTH or x2<0 or x2>WIDTH or y1<0 or y1>HEIGHT or y2<0 or y2>HEIGHT:
        twhcolors.cyclecolor()
        reset()

    pygame.draw.line(screen, twhcolors.getColor(), (x1, y1), (x2, y2), LINESTYLE)
    pygame.draw.circle(screen, twhcolors.getColor(), (x2, y2), 5, 0)

    #update display
    pygame.display.flip()
