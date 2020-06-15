
#Description
#A stranger form of spiral
#Demonstrates polar to cartesian conversion
#https://www.mathsisfun.com/polar-cartesian-coordinates.html
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *
from math import *
import twhcolors

#Frames pr second
FPS=25

#window size
WIDTH=800
HEIGHT=800

#center x,y and radius
CENTERX=400
CENTERY=400

#change these 4 constants to get som wierd patterns
STARTTHETA=1
STARTRADIUS=1
DELTATHETA=0.002
DELTARADIUS=1.03

# Physical properties and initial conditions for spiral
# initial upper angle (from vertical)
theta=radians(0)

# start spiral at rest
theta1=STARTTHETA
theta2=0
radius=STARTRADIUS
startx=CENTERX
starty=CENTERY

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
screen.fill(pygame.Color("gray69"))

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
    # Change theta
    theta1+=DELTATHETA
    #Change angle with theta1
    theta2-=theta1
    #calculate new position for the ball
    stopx=CENTERX+int(radius*sin(theta2))
    stopy=CENTERY-int(radius*cos(theta2))

    #draw new pendulum
    pygame.draw.circle(screen, pygame.Color("black"), (stopx, stopy), 2, 0)
    pygame.draw.line(screen, pygame.Color("black"), (startx, starty), (stopx, stopy), 2)

    #flip start and stop
    startx=stopx
    starty=stopy

    #update display
    pygame.display.flip()
