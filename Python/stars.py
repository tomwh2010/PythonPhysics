##############################################################################
#Description
#moving thru a galaxy  full of stars
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors
import twhwindow
import random

##############################################################################
#constants
##############################################################################
#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

#Frames pr second; i.e. speed of starship
FPS=45

#window size
WIDTH=600
HEIGHT=600

#center window
CENTERX=WIDTH//2
CENTERY=HEIGHT//2

#chance of new star
CHANCE=5

#initial number of stars
STARS0=50

##############################################################################
#variables
##############################################################################
#list of stars
stars=[]

##############################################################################
#functions
##############################################################################
#generate our first collection of stars
def generatestars0():
    for i in range(STARS0):
        #how far from the center
        r=random.randint(0, 500)
        #at which angle
        theta=random.randint(0, 359)
        #add star to list
        star=[r, theta]
        stars.append(star)

#draw the Stars
def drawstars():
    for index, element in enumerate(stars):
        #calculate x,y from r,theta using polar->cartesian conversion
        x=CENTERX+int(element[0]*cos(element[1]))
        y=CENTERY+int(element[0]*sin(element[1]))

        #if a star is out-of-bounds then remove it from the list
        if x<0 or x>WIDTH or y<0 or y>HEIGHT:
            stars.pop(index)
        else:
            #draw the star
            pygame.draw.circle(screen, twhcolors.WHITE, (x, y), 3, FILLSTYLE)

#move stars outwards and add a new star
def fly():
    #increase r for each star by 1
    #i.e. move outward
    for i in stars:
        i[0]+=1

    #add a star
    doit=random.randint(0,100)
    if doit<CHANCE:
        theta=random.randint(0, 359)
        star=[0, theta]
        stars.append(star)

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

#generate our first batch of stars
generatestars0()

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

    #draw background color to blank the screen
    screen.fill(twhcolors.BLACK)

    #fly thru space!
    drawstars()
    #create text buffer
    strBuffer="Stars #"+str(len(stars))
    twhwindow.drawinfobox(screen, myfont, WIDTH, HEIGHT, 110, 20, -10, -10, strBuffer, twhcolors.WHITE, twhcolors.BLACK, FILLSTYLE)
    fly()

    #update display
    pygame.display.flip()
