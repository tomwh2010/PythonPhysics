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
import random

##############################################################################
#constants
##############################################################################
SHAPE_COLOR=twhcolors.RED

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

FPS=40 #Frames pr second

#window size
WIDTH=600
HEIGHT=600
CENTERX=WIDTH//2
CENTERY=HEIGHT//2

STARDELTA=1
CHANCE=5
STARS0=50

##############################################################################
#variables
##############################################################################
stars=[]

##############################################################################
#functions
##############################################################################
#generate our first collection of stars
def generatestars0():
    for i in range(STARS0):
        r=random.randint(0, 500)
        theta=random.randint(0, 359)
        star=[r, theta]
        stars.append(star)

#draw the Stars
def drawstars():
    for index, element in enumerate(stars):
        #calculate x,y from r,theta using polar->certasian conversion
        x=CENTERX+int(element[0]*cos(element[1]))
        y=CENTERY+int(element[0]*sin(element[1]))

        if x<0 or x>WIDTH or y<0 or y>HEIGHT:
            #if a star is out-of-bounds then remove it from the list
            stars.pop(index)
        else:
            #draw the star
            pygame.draw.circle(screen, twhcolors.WHITE, (x, y), 3, FILLSTYLE)

def drawinfo():
    pygame.draw.rect(screen, twhcolors.BLACK, (WIDTH-130, HEIGHT-40, 200, 100), FILLSTYLE)
    #create text buffer
    strBuffer="Stars #"+str(len(stars))
    #render buffer as picture
    textsurface=myfont.render(strBuffer, 1, twhcolors.WHITE)
    #paint picture to screen at location 130,180
    screen.blit(textsurface,(WIDTH-110, HEIGHT-30))


def fly():
    #increase r for each star by STARDELTA
    #i.e. move outward
    for i in stars:
        i[0]+=STARDELTA

    #add a star
    doit=random.randint(0,100)
    if doit<CHANCE:
        theta=random.randint(0, 359)
        star=[0, theta]
        stars.append(star)
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
    screen.fill(twhcolors.MAROON)

    drawstars()
    drawinfo()
    fly()

    #update display
    pygame.display.flip()
