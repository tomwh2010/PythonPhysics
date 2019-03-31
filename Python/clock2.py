##############################################################################
#Description
#Draw an analog clock
#Demonstrates polar to cartesian conversion
#Alternative version; smooth transitions
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import datetime
import twhcolors

##############################################################################
#constants
##############################################################################
#Frames pr second
FPS=20

#window size
WIDTH=400
HEIGHT=420

#center x,y and radius
STARTX=200
STARTY=200

#hand radius
RADIUS_HOUR=150
RADIUS_MINUTE=190
RADIUS_SECOND=190

#hand color
COLOR_HOUR=twhcolors.BLACK
COLOR_MINUTE=twhcolors.BLACK
COLOR_SECOND=twhcolors.BLUE

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

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont = pygame.font.SysFont('Courier', 12)

# set up the window with size and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Clock2')

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

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #fetch clock
    now=datetime.datetime.now()
    micro=now.microsecond
    second=now.second+micro/1000000.0
    minute=now.minute+second/60
    hour=now.hour+minute/60

    #calculate theta
    theta_second=radians(second*360/60)
    theta_minute=radians(minute*360/60)
    theta_hour=radians(hour*360/12)

    #calculate stopx, stopy for each hand
    stopx_hour=STARTX+int(RADIUS_HOUR*sin(theta_hour))
    stopy_hour=STARTY-int(RADIUS_HOUR*cos(theta_hour))

    stopx_minute=STARTX+int(RADIUS_MINUTE*sin(theta_minute))
    stopy_minute=STARTY-int(RADIUS_MINUTE*cos(theta_minute))

    stopx_second=STARTX+int(RADIUS_SECOND*sin(theta_second))
    stopy_second=STARTY-int(RADIUS_SECOND*cos(theta_second))

    #paint clock hands
    pygame.draw.line(screen, COLOR_HOUR, (STARTX, STARTY), (stopx_hour, stopy_hour), 3)
    pygame.draw.line(screen, COLOR_MINUTE, (STARTX, STARTY), (stopx_minute, stopy_minute), 3)
    pygame.draw.line(screen, COLOR_SECOND, (STARTX, STARTY), (stopx_second, stopy_second))
    pygame.draw.circle(screen, twhcolors.BLACK, (STARTX, STARTY), 5, 0)

    #write text to screen
    strBuffer="Current time: "+now.strftime("%a, %d %b %Y %H:%M:%S +0000")
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(10,400))

    #update display
    pygame.display.flip()
