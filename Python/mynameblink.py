##############################################################################
#Description
#Draw a simple blinking string
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
#Frames pr second
FPS=1

#window size
WIDTH=400
HEIGHT=400

##############################################################################
#variables
##############################################################################
#status flag to show text or not
blinkit=False
#create text buffer
strBuffer="My name is Tom"

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
pygame.display.set_caption('Framework')

# creates a clock
clock=pygame.time.Clock()

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 24)

#render buffer as picture
textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)

##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    #I paint the background here instead to blank the screen for each frame
    screen.fill(twhcolors.SILVER)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #if blinkit is true then shwo name
    if blinkit:
        #paint picture to screen at location 130,180
        screen.blit(textsurface,(130, 180))
        blinkit=False
    else:
        blinkit=True

    #update display
    pygame.display.flip()
