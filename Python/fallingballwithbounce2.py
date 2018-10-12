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
M=0.5 #mass in kg
K=0.1 #air resistance in Nss/m/m

#initial velocity
STARTVELOCITY=.1

#fraction height
DAMPER=0.85

#inital x-position
XPOS0=50.0

#
XFORWARDMOTION=0.0

##############################################################################
#variables
##############################################################################
velocity=STARTVELOCITY
direction=1.0 #start with falling down
ypos=10.0 #inital y-position
xpos=XPOS0

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

#screen.fill(twhcolors.SILVER)
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
        xpos+=XFORWARDMOTION
        acceleration=G-K*velocity**2/M
        velocity=velocity+acceleration*dt
        ypos+=direction*velocity

        # Change velocity according to accelleration
#        velocity+=direction*G*dt

        #if the ball has lost upward motion
        if velocity<0.01:
            velocity=0.0
            direction=1.0

        #if we hit rock bottom then change to up
        if ypos>=476.0:
            ypos=476.0
            direction=-1.0
            velocity=velocity*DAMPER

        print(str(round(acceleration, 2)), str(round(direction, 1)), str(round(velocity, 2)), str(round(ypos, 2)))

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, (int(xpos), int(ypos)), 5, FILLSTYLE)

    #update display
    pygame.display.flip()
