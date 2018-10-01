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
FPS=40 #Frames pr second

#window size
WIDTH=400
HEIGHT=420

##############################################################################
#variables
##############################################################################

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygam environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

#draw background color to blank the screen
screen.fill(twhcolors.PINK)

# creates a clock
clock=pygame.time.Clock()

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

    #update display
    pygame.display.update()
