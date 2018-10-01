##############################################################################
#Purpose
#Draw an analog clock
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
from time import gmtime, strftime, localtime
import twhcolors

##############################################################################
#functions
##############################################################################
def drawclockhand(stopx, stopy, center, pendulum):
    pygame.draw.circle(screen, center, (STARTX, STARTY), 5, 0)
    pygame.draw.line(screen, pendulum, (STARTX, STARTY), (stopx, stopy))

##############################################################################
#constants
##############################################################################
FPS=40 #Frames pr second

#window size
WIDTH=400
HEIGHT=420

#center x,y and rod length
STARTX=200
STARTY=200

LENGTH_HOUR=150
LENGTH_MINUTE=190
LENGTH_SECOND=190

COLOR_HOUR=twhcolors.BLACK
COLOR_MINUTE=twhcolors.RED
COLOR_SECOND=twhcolors.BLUE

##############################################################################
#variables
##############################################################################

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment
pygame.font.init() # you have to call this at the start if you want to use this module.

#choose font for later use
myfont = pygame.font.SysFont('Courier', 12)

# set up the window with size and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Clock')

# creates a clock
clock=pygame.time.Clock()

##############################################################################
#main loop
##############################################################################

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill(twhcolors.SILVER)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #fetch  clock
    theclock=localtime()

    #calculate theta
    theta_second=radians(theclock[5]*360/60)
    theta_minute=radians((theclock[4]+theclock[5]/60)*360/60)
    theta_hour=radians((theclock[3]+theclock[4]/60)*360/12)

    #calculate stopx, stopy for each hand
    stopx_hour=STARTX+int(LENGTH_HOUR*sin(theta_hour))
    stopy_hour=STARTY-int(LENGTH_HOUR*cos(theta_hour))

    stopx_minute=STARTX+int(LENGTH_MINUTE*sin(theta_minute))
    stopy_minute=STARTY-int(LENGTH_MINUTE*cos(theta_minute))

    stopx_second=STARTX+int(LENGTH_SECOND*sin(theta_second))
    stopy_second=STARTY-int(LENGTH_SECOND*cos(theta_second))

    #paint clock hands
    drawclockhand(stopx_hour,   stopy_hour,   twhcolors.BLACK, COLOR_HOUR)
    drawclockhand(stopx_minute, stopy_minute, twhcolors.BLACK, COLOR_MINUTE)
    drawclockhand(stopx_second, stopy_second, twhcolors.BLACK, COLOR_SECOND)

    #write text to screen
    strBuffer="Current time: "+strftime("%a, %d %b %Y %H:%M:%S +0000", localtime())
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(10,400))

    #update display and wait
    pygame.display.update()
