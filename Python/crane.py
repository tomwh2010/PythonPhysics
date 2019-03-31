##############################################################################
#Description
#A simple game about a crane
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors

##############################################################################
#constants (variable names written with upper case)
##############################################################################
FPS=40 #Frames pr second

#window size
WIDTH=1200
HEIGHT=600

CRANE_Y0=478
CRANE_XOFFSET=81

FAR_LEFT=10
FAR_RIGHT=500

DELTA_CAR=10

DELTA_ARM=10
ARM_LOW=15
ARM_HIGH=65

DELTA_WIRE=5

##############################################################################
#variables
##############################################################################
#cranearms=[[200, 45, 0, 0], [150, 90, 0, 0], [100, 135, 0, 0], [30, 0, 0, 0], [0, 0, 0, 0]] #radius, theta, x, y

cranerects=[[FAR_LEFT, 500, 300, 80], [FAR_LEFT+10, 450, 150, 50]]
cranecircles=[]

def drawcrane():
    global crane, screen
    #car
    pygame.draw.rect(screen, twhcolors.BLUE, cranerects[0], 0)
    #cranehouse
    pygame.draw.rect(screen, twhcolors.RED, cranerects[1], 0)
    #cockpit
    #pointlist=[(car_left+210, 450), (car_left+210, 500), (car_left+300, 500)]
    #pygame.draw.polygon(screen, twhcolors.GRAY, pointlist, 0)
    #wheels
    #pygame.draw.circle(screen, twhcolors.BLACK, (car_left+40, 578), 20, 0)
    #pygame.draw.circle(screen, twhcolors.BLACK, (car_left+240, 578), 20, 0)

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

# creates a clock
clock=pygame.time.Clock()

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 24)

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

    #calculatexy()
    drawcrane()

    #update display
    pygame.display.flip()
