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
import pygame.gfxdraw

##############################################################################
#constants
##############################################################################
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0
LINESTYLE=1

FPS=40 #Frames pr second

#window size
WIDTH=1100
HEIGHT=700

# gravity
G=9.81

#initial velocity
STARTVELOCITY=.1

#inital x-position
XPOS0=50.0

#
XFORWARDMOTION=2

##############################################################################
#variables
##############################################################################
velocity=STARTVELOCITY
direction=1.0 #start with falling down
ypos=10.0 #inital y-position
xpos=XPOS0
yposlow=ypos
#fraction height
damper=0.85
damperdamper=1.05

#delta time
dt=0.1

#animation is running?
animation=False

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

screen.fill(twhcolors.SILVER)
##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    #screen.fill(twhcolors.SILVER)

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
        xpos+=XFORWARDMOTION
        #calculate new position for the ball
        ypos+=direction*velocity

        # Change velocity according to accelleration
        velocity+=direction*G*dt

        #if the ball has lost upward motion
        if velocity<0.01:
            velocity=0.0
            direction=1.0
            yposlow=ypos
            damper/=damperdamper

        #if we hit rock bottom then change to up
        if ypos>676.0:
            ypos=676.0
            if abs(ypos-yposlow)<1:
                animation=False
            else:
                direction=-1
                velocity*=damper

        print(str(round(yposlow, 2)), str(round(ypos, 2)), str(round(direction, 1)), str(round(velocity, 2)))

    #fade previous balls
    pygame.gfxdraw.box(screen, pygame.Rect(0,0,WIDTH,HEIGHT), (255,255,255,7))

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, (int(xpos), int(ypos)), 5, FILLSTYLE)

    #update display
    pygame.display.flip()
