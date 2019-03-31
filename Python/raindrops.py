##############################################################################
#Description
#Raindrops on a window
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors
import pygame.gfxdraw
import random
import twhsplash

twhsplash.splash("Raindrops")

##############################################################################
#constants
##############################################################################
#Frames pr second
FPS=20

#window size
WIDTH=600
HEIGHT=600
DELTACONST=1

#center x,y and radius
RADIUS=WIDTH//2//2
CENTERY=HEIGHT//2
CELLSIZE=2

assert WIDTH%CELLSIZE==0, "Wrong width, cellsize"
assert HEIGHT%CELLSIZE==0, "Wrong height, cellsize"

#calculate cellwidth,cellheight
CELLWIDTH=WIDTH//CELLSIZE
CELLHEIGHT=HEIGHT//CELLSIZE

##############################################################################
#variables
##############################################################################
#initial angle
raindrops=[[0 for i in range(CELLWIDTH)] for j in range(CELLHEIGHT)]
angle=0
allmost=False

counter=0

#initial x, y for ball
centerx=WIDTH//2//2
centerx0=centerx
centerx1=centerx0+2*RADIUS
ballx=centerx
bally=CENTERY-RADIUS
#change to negative number for counterclockwise
delta=DELTACONST

##############################################################################
#functions
##############################################################################
#create initial life
def createraindrops():
    for x in range(CELLWIDTH):
        for y in range(CELLHEIGHT):
            if raindrops[x][y]<10:
                raindrops[x][y]=random.randint(0, 1000)

#draw each cell
def drawrain():
    for x in range(CELLWIDTH):
        for y in range(CELLHEIGHT):
            if raindrops[x][y]>998:
                pygame.draw.circle(screen, twhcolors.LIGHTGRAY, (x*CELLSIZE, y*CELLSIZE), 4, 0)

def gravity():
    for x in range(CELLWIDTH-1, -1, -1):
        for y in range(CELLHEIGHT-2, -1, -1):
            if random.randint(0, 100)>0:
                t=raindrops[x][y]
                raindrops[x][y]=0
                raindrops[x][y+1]=t

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Raindrops')

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)
createraindrops()

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

    #add smoke
    pygame.gfxdraw.box(screen, pygame.Rect(0,0,WIDTH,HEIGHT), (255,255,255,30))

    gravity()
    drawrain()
    createraindrops()

    #update display
    pygame.display.flip()
