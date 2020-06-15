#Description
#Ball moves in a circle
#Polar to cartesian conversion
#https://www.mathsisfun.com/polar-cartesian-coordinates.html
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *
from math import *

#Frames pr second
FPS=24

#window size
WIDTH=400
HEIGHT=400

#center x,y and radius
CENTERX=WIDTH//2
CENTERY=HEIGHT//2
RADIUS=190

#change to negative number for counterclockwise
DELTA=1

#initial angle
angle=0

#initial x, y for ball
ballx=CENTERX
bally=CENTERY-RADIUS

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Circle')

# creates a clock
clock=pygame.time.Clock()

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill(pygame.Color("gray69"))

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #paint ball
    pygame.draw.circle(screen, pygame.Color("black"), (ballx, bally), 5, 0)

    #update angle
    angle+=DELTA
    theta=radians(angle)

    #calculate x,y for ball
    ballx=CENTERX+int(RADIUS*sin(theta))
    bally=CENTERY-int(RADIUS*cos(theta))

    #update display
    pygame.display.flip()
