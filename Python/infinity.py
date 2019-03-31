##############################################################################
#Description
#Ball moves in a figure eight with trailing smoke
#Polar to cartesian convversion
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors
import pygame.gfxdraw
from math import radians, cos, sin
import twhsplash

twhsplash.splash("Infinity")

##############################################################################
#constants
##############################################################################
#Frames pr second
FPS=60

#window size
WIDTH=771
HEIGHT=400

DELTACONST=1

#center x,y and radius
RADIUS=HEIGHT//2-10
CENTERY=HEIGHT//2+5

##############################################################################
#variables
##############################################################################
#initial angle
angle=0
allmost=False

counter=0

#initial x, y for ball
centerx=WIDTH//2//2
centerx0=centerx
centerx1=centerx0+2*RADIUS
ballx=centerx
bally=CENTERY-RADIUS

#change to negative number for counterclockwise
delta=DELTACONST

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
pygame.display.set_caption('Inifinity')

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

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

    #add smoke
    pygame.gfxdraw.box(screen, pygame.Rect(0,0,WIDTH,HEIGHT), (255,255,255,4))

    #paint ball
    pygame.draw.circle(screen, twhcolors.BLACK, (ballx, bally), 8, 0)
    pygame.gfxdraw.aacircle(screen, ballx, bally, 8, twhcolors.BLACK)

    #update angle
    angle+=delta
    theta=radians(angle)

    #calculate x,y for ball
    ballx=centerx+int(RADIUS*sin(theta))
    bally=CENTERY-int(RADIUS*cos(theta))

    #normalize angle
    if angle<0:
        angle=358
    if angle>360:
        angle=0

    #prepare change of radius and delta
    if angle==272 and centerx==centerx1:
        allmost=True

    if angle==88 and centerx==centerx0:
        allmost=True

    #change radius and delta
    if angle==270 and allmost:
        delta=DELTACONST
        centerx=centerx0
        angle=90
        allmost=False

    if angle==90 and allmost:
        delta=-DELTACONST
        centerx=centerx1
        angle=270
        allmost=False

    #update display
    pygame.display.flip()
