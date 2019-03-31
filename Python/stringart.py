##############################################################################
#Description
#make a circle with circle(i.e. nail at each angle 0-359)
#start at arbitrary circle
#draw string between 2 circles/nails
#increase by certain amount
#stop if stopangle=0
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
FPS=4

#window size
WIDTH=600
HEIGHT=600

#center x,y and radius
CENTERX=WIDTH//2
CENTERY=HEIGHT//2
RADIUS=190

DELTA=2
SLOTS=40
STEPS=360//SLOTS

##############################################################################
#variables
##############################################################################
#initial angle
angle0=0
angle1=19
step=11

nails=[]

for angle in range(SLOTS):
    theta=radians(angle*STEPS)

    #calculate x,y for ball
    stopx=CENTERX+int(RADIUS*sin(theta))
    stopy=CENTERY-int(RADIUS*cos(theta))
    nails.append([stopx, stopy])

print(nails)
##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Circle')

# creates a clock
clock=pygame.time.Clock()

##############################################################################
#main loop
##############################################################################

for angle in nails:
    pygame.draw.circle(screen, twhcolors.WHITE, (angle[0], angle[1]), 5, 0)

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

    pygame.draw.line(screen, twhcolors.getColor(), (nails[angle0][0], nails[angle0][1]), (nails[angle1][0], nails[angle1][1]), 1)
    print(angle0, angle1)
    angle0+=step
    angle1+=step
    if angle0>=SLOTS:
        angle0-=SLOTS
    if angle1>=SLOTS:
        angle1-=SLOTS
    if angle0==0:
        twhcolors.cyclecolor()


    #update display
    pygame.display.flip()
