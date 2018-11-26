##############################################################################
#Description
#Maze
#Bits
#0000 0001 Up
#0000 0010 right
#0000 0100 down
#0000 1000 left
#0001 0000 start
#0010 0000 stop
#0100 0000 mark
#1000 0000 robot
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
WIDTH=600
HEIGHT=700

##############################################################################
#variables
##############################################################################
maze=[[9, 5, 5, 3, 9, 39], [12, 5, 3, 12, 2, 11], [9, 3, 8, 3, 10, 10], [30, 12, 6, 14, 12, 6]]
print(maze)

##############################################################################
#functions
##############################################################################
def printmaze():
    pass
    
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
