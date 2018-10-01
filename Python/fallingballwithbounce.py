##############################################################################
#Purpose
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors

##############################################################################
#functions
##############################################################################

##############################################################################
#constants
##############################################################################
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0
LINESTYLE=1

FPS=40 #Frames pr second

#window size
WIDTH=800
HEIGHT=500

# gravity
G=9.81

#initial velocity
STARTVELOCITY=.1

#fraction height
DAMPER=0.99

#inital x-position
XPOS=400

##############################################################################
#variables
##############################################################################
velocity=STARTVELOCITY
direction=1 #start with falling down
ypos=30 #inital y-position
yposold=ypos
miny=ypos-1

#delta time and initial time
dt=0.1
t=0.

#animation is running?
animation=False

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

        # if any key is pressed
        elif event.type==pygame.KEYDOWN:
            #start animation
            animation=True

    if animation:
        #calculate new position for the ball
        yposold=ypos
        ypos+=direction*velocity*dt

        # Change velocity according to accelleration
        velocity+=direction*G*dt
        if direction<0:
            velocity*=DAMPER

        if round(ypos)==round(yposold):
            direction=1

        #if we hit rock bottom then change to up
        if ypos>476.0:
            direction=-1
        print(str(round(ypos)), direction, str(round(velocity)))

        #update time
        t=t+dt

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, (XPOS, int(ypos)), 20, FILLSTYLE)

    #update display
    pygame.display.update()
