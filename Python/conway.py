##############################################################################
#Description
#Conway's Game Of Life
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors
import random

##############################################################################
#constants
##############################################################################
#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0
LINESTYLE=4

FPS=1 #Frames pr second

#window size
WIDTH=600
HEIGHT=600
CELLSIZE=10

assert WIDTH%CELLSIZE==0, "Wrong width, cellsize"
assert HEIGHT%CELLSIZE==0, "Wrong height, cellsize"

CELLWIDTH=WIDTH//CELLSIZE
CELLHEIGHT=HEIGHT//CELLSIZE

##############################################################################
#variables
##############################################################################
#initialize lists
life=[[0 for i in range(CELLWIDTH)] for j in range(CELLHEIGHT)]
gen=[[0 for i in range(CELLWIDTH)] for j in range(CELLHEIGHT)]

##############################################################################
#functions
##############################################################################
def createlife():
    for x in range(1, CELLWIDTH-1):
        for y in range(1, CELLHEIGHT-1):
            life[x][y]=random.randint(0, 1)

def drawgrid():
    #draw cells
    for x in range(CELLWIDTH):
        for y in range(CELLHEIGHT):
            if life[x][y]==1:
                pygame.draw.rect(screen, twhcolors.WHITE, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE), 0)

    #horizontal lines
    for i in range(CELLWIDTH):
        pygame.draw.line(screen, twhcolors.BLACK, (0, i*CELLSIZE), (WIDTH, i*CELLSIZE), 1)

    #vertical lines
    for i in range(CELLHEIGHT):
        pygame.draw.line(screen, twhcolors.BLACK, (i*CELLSIZE, 0), (i*CELLSIZE, HEIGHT), 1)

def newgeneration():
    for x in range(1, CELLWIDTH-1):
        for y in range(1, CELLHEIGHT-1):
            gen[x][y]=0
            neighbors=0
            center=0
            for x1 in range(-1, 2):
                for y1 in range(-1, 2):
                    if x1==0 and y1==0:
                        center=life[x][y]
                    else:
                        neighbors+=life[x+x1][y+y1]
            if (neighbors==2 or neighbors==3) and center==1:
                #print(x,y,center,neighbors)
                gen[x][y]=1
            if neighbors==3 and center==0:
                #print(x,y,center,neighbors)
                gen[x][y]=1
    for x in range(1, CELLWIDTH-1):
        for y in range(1, CELLHEIGHT-1):
            life[x][y]=gen[x][y]
    #Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    #Any live cell with two or three live neighbors lives on to the next generation.
    #Any live cell with more than three live neighbors dies, as if by overpopulation.
    #Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Conway Game Of Life')

# creates a clock
clock=pygame.time.Clock()

createlife()
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
    screen.fill(twhcolors.SILVER)

    drawgrid()
    newgeneration()

    #update display
    pygame.display.flip()
