
#Description
#Spiral is a ball that moves in a circle with increasing/decreasing radius
#Demonstrates polar to cartesian conversion
#https://www.mathsisfun.com/polar-cartesian-coordinates.html
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *
from math import *
from twhcolors import *

#2 pixel thick line
LINESTYLE=2

#Frames pr second
FPS=50

#window size
WIDTH=600
HEIGHT=600

#center x,y
CENTERX=WIDTH//2
CENTERY=HEIGHT//2

#change these two to change the spiral size
DELTARADIUS=0.05
DELTAANGLE=6.0

#start, end points for ball and line
startx=0
starty=0
stopx=0
stopy=0

#angle and radius for ball
angle=0
radius=0

#reset if ball hits the edge
def resetvars():
    global startx, starty, stopx, stopy, angle, radius
    startx=CENTERX
    starty=CENTERY
    stopx=CENTERX
    stopy=CENTERY
    angle=0
    radius=1

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lines')

#draw background color to blank the screen
screen.fill(pygame.Color("gray69"))

# creates a clock
clock=pygame.time.Clock()

#reset the variables
resetvars()

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #calculate angle and radius
    angle+=DELTAANGLE
    radius+=DELTARADIUS
    if angle==360:
        angle=0
    theta=radians(angle)

    #calculate new start, end points
    startx=stopx
    starty=stopy
    stopx=startx+int(radius*sin(theta))
    stopy=starty-int(radius*cos(theta))

    #if reached the edge then reset coords and choose new color
    if startx<0 or startx>WIDTH or stopx<0 or stopx>WIDTH or starty<0 or starty>HEIGHT or stopy<0 or stopy>HEIGHT:
        cyclecolor()
        resetvars()

    #draw line and ball
    pygame.draw.line(screen, getColor(), (startx, starty), (stopx, stopy), LINESTYLE)
    pygame.draw.circle(screen, getColor(), (stopx, stopy), 5, 0)

    #update display
    pygame.display.flip()
