##############################################################################
#Purpose
#Draw a simple string
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors

##############################################################################
#functions
##############################################################################

##############################################################################
#constants
##############################################################################
FPS=40 #Frames pr second

#window size
WIDTH=400
HEIGHT=400

##############################################################################
#variables
##############################################################################

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

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

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #create text buffer
    strBuffer="My name is Tom"
    #render buffer as picture
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    #paint picture to screen at location 130,180
    screen.blit(textsurface,(130,180))

    #update display
    pygame.display.update()
