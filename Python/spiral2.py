##############################################################################
#Description
#Draw a spiral version 2
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
#Frames pr second
FPS=25

#window size
WIDTH=800
HEIGHT=800

#center x,y and radius
CENTERX=400
CENTERY=400

#change these 4 constants to get som wierd patterns
STARTVELOCITY=1
STARTRADIUS=1
DELTAVELOCITY=0.002
DELTARADIUS=1.03

##############################################################################
#variables
##############################################################################
# Physical properties and initial conditions for pendulum
# initial upper angle (from vertical)
theta=radians(0)
# start pendulum at rest
velocity=STARTVELOCITY
radius=STARTRADIUS
startx=CENTERX
starty=CENTERY

##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# you have to call this at the start if you want to use this module.
pygame.font.init()

# creates a clock
clock=pygame.time.Clock()

#choose font for later use
myfont = pygame.font.SysFont('Courier', 12)

# set up the window with size and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spiral')


#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

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

    # Calculate new radius
    radius*=DELTARADIUS
    # Change velocity
    velocity+=DELTAVELOCITY
    # Change angle according to (updated) velocity
    theta-=velocity
    #calculate new position for the ball
    stopx=CENTERX+int(radius*sin(theta))
    stopy=CENTERY-int(radius*cos(theta))

    #draw new pendulum
    pygame.draw.circle(screen, twhcolors.BLACK, (stopx, stopy), 2, 0)
    pygame.draw.line(screen, twhcolors.BLACK, (startx, starty), (stopx, stopy), 2)

    #flip start and stop
    startx=stopx
    starty=stopy

    #update display
    pygame.display.flip()
