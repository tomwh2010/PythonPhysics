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
FPS=4 #Frames pr second

#window size
WIDTH=400
HEIGHT=400

TEXTON=FPS
TEXTOFF=FPS*2

##############################################################################
#variables
##############################################################################

##############################################################################
#functions
##############################################################################

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
i=0

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

    i+=1

    if i<TEXTON:
        #create text buffer
        strBuffer="My name is Tom"
        #render buffer as picture
        textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
        #paint picture to screen at location 130,180
        screen.blit(textsurface,(130, 180))

    if i==TEXTOFF:
        i=0

    #update display
    pygame.display.flip()
