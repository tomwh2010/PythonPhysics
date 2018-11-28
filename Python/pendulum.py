##############################################################################
#Description
#Pendulum
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
FPS=15

#window size
WIDTH=400
HEIGHT=420

#center x,y and radius
STARTX=200
STARTY=200
RADIUS=190

# gravity
G=9.81

#Start angle and velocity
#0=up, 90=right, 180=down, 270=left
#Try different angles to see what happens
STARTANGLE=5

#>0 =>counter-clockwise
#<0 =>clockwise
#otherwise side to side
#higher initial velocity=>higher speed
STARTVELOCITY=0

#Try this instead. You will get a clockwise motion where the pendulum will
#ever so slightly make full rotation
#STARTANGLE=5
#STARTVELOCITY=-0.002

##############################################################################
#variables
##############################################################################
# Physical properties and initial conditions for pendulum
# initial upper angle (from vertical)
theta=radians(STARTANGLE)

# start pendulum at start
velocity=STARTVELOCITY

#delta time
dt=0.1

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
pygame.display.set_caption('Pendelum')

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

    # Calculate accelleration due to gravity
    accel=-(G/RADIUS)*sin(theta)
    # Change velocity according to accelleration
    velocity+=accel*dt
    # Change angle according to (updated) velocity
    theta-=velocity

    #calculate new position for the ball
    stopx=STARTX+int(RADIUS*sin(theta))
    stopy=STARTY-int(RADIUS*cos(theta))

    #calculate angle in degrees
    currentangle=abs(degrees(theta))%360
    if STARTVELOCITY>0:
        currentangle=360-currentangle

    #write text to screen
    strBuffer="Current angle: "+str(int(currentangle))+" Velocity: "+str(round(abs(velocity)*100, 2))
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(10,400))

    #draw new pendulum
    pygame.draw.line(screen, twhcolors.BLUE, (STARTX, STARTY), (stopx, stopy))
    pygame.draw.circle(screen, twhcolors.RED, (stopx, stopy), 5, 0)
    pygame.draw.circle(screen, twhcolors.BLACK, (STARTX, STARTY), 5, 0)

    #update display
    pygame.display.flip()
