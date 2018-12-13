##############################################################################
#Description
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
#color of the ball
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

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
pygame.display.set_caption('Move a ball')

# creates a clock
clock=pygame.time.Clock()

#initial location of the ball; center
myball=[WIDTH//2, HEIGHT//2]

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

    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[K_LEFT]:
        myball[0]-=5

    if keys_pressed[K_RIGHT]:
        myball[0]+=5

    if keys_pressed[K_UP]:
        myball[1]-=5

    if keys_pressed[K_DOWN]:
        myball[1]+=5

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, myball, 10, FILLSTYLE)

    #update display
    pygame.display.flip()
