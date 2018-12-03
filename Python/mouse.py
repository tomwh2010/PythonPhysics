##############################################################################
#Description
#Draw a square; change color with mouse movement and click
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors

##############################################################################
#constants
##############################################################################
#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0

#Frames pr second
FPS=25

#window size
WIDTH=600
HEIGHT=620

YELLOW=(255,255,0)
RED=(255,0,0)
GREEN=(0,128,0)
BLUE=(0,0,255)

##############################################################################
#variables
##############################################################################
chosen=False
box=pygame.Rect(100, 100, 300, 300)

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
pygame.display.set_caption('Mouse')

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

    x,y=pygame.mouse.get_pos()
    collision=False
    if box.collidepoint(x, y):
        collision=True

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        #if user clicked on the square->change state
        elif event.type == MOUSEBUTTONUP:
            if collision:
                chosen=not chosen

    if chosen:
        if collision:
            color=YELLOW
        else:
            color=BLUE
    else:
        if collision:
            color=RED
        else:
            color=GREEN

    pygame.draw.rect(screen, color, box, FILLED)

    #update display
    pygame.display.flip()
