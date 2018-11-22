##############################################################################
#Description
#Maze
#Bits
#0 Up
#10 right
#100 down
#1000 left
#10000 start
#100000 stop
#1000000 mark
#10000000 robot
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors

##############################################################################
#constants (variable names written with upper case)
##############################################################################
#Frames pr second
FPS=40

#window size
WIDTH=800
HEIGHT=600

##############################################################################
#variables
##############################################################################

##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze')

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

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
    pygame.display.flip()
