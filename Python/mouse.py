##############################################################################
#Description
#Draw different objects
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
FRAMED=1
LINESTYLE=4

#Frames pr second
FPS=40

#window size
WIDTH=600
HEIGHT=620

##############################################################################
#variables
##############################################################################
chosen=False

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

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        #if user clicked on the square->change state
        elif event.type == pygame.MOUSEBUTTONUP:
            x,y = pygame.mouse.get_pos()
            if x>=100 and x<=400 and y>=100 and y<=400:
                chosen=not chosen

    #is the mouse within the boundaries of the square->set the appropriate color
    x, y=pygame.mouse.get_pos()
    color=twhcolors.YELLOW
    if chosen:
        color=twhcolors.GREEN
    if x>=100 and x<=400 and y>=100 and y<=400:
        color=twhcolors.BLUE
        if chosen:
            color=twhcolors.RED
            
    #rect(screen, color, coords(top, left, width, height), fillstyle
    pygame.draw.rect(screen, color, (100, 100, 300, 300), FILLED)

    #update display
    pygame.display.flip()
