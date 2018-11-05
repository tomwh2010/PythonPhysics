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
WIDTH=800
HEIGHT=500

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
pygame.display.set_caption('Framework')

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

    #circle(screen, color, coords(x, y), radius, fillstyle
    pygame.draw.circle(screen, twhcolors.RED, (405, 405), 40, FILLED)

    #rect(screen, color, coords(top, left, width, height), fillstyle
    pygame.draw.rect(screen, twhcolors.YELLOW, (125, 225, 100, 100), FILLED)

    #ellipse(screen, color, coords(top, left, bottom, right), fillstyle
    pygame.draw.ellipse(screen, twhcolors.BLUE, (325, 25, 450, 100), FRAMED)

    #polygon(screen, color, pointlist((x, y)...), fillstyle
    pointlist_1 = [(25, 25), (105, 185), (185, 25)]
    pygame.draw.polygon(screen, twhcolors.GREEN, pointlist_1, FRAMED)

    #line(screen, color, coords1(x, y), coords2(x, y), fillstyle
    pygame.draw.line(screen, twhcolors.MAGENTA, (25, 200), (375, 200), LINESTYLE)

    #update display
    pygame.display.flip()
