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
import twhwindow
import random

##############################################################################
#constants
##############################################################################
#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0
LINESTYLE=4

#Frames pr second
FPS=4

#window size
WIDTH=600
HEIGHT=600
CELLSIZE=10

assert WIDTH%CELLSIZE==0, "Wrong width, cellsize"
assert HEIGHT%CELLSIZE==0, "Wrong height, cellsize"

#calculate cellwidth,cellheight
CELLWIDTH=WIDTH//CELLSIZE
CELLHEIGHT=HEIGHT//CELLSIZE

##############################################################################
#variables
##############################################################################
#initialize life and nextgen lists
life=[[0 for i in range(CELLWIDTH)] for j in range(CELLHEIGHT)]
gen=[[0 for i in range(CELLWIDTH)] for j in range(CELLHEIGHT)]

#number of generations
generation=0

##############################################################################
#functions
##############################################################################
#create initial life
def createlife():
    x0=1
    x1=CELLWIDTH-1
    y0=1
    y1=CELLHEIGHT-1

    for x in range(x0, x1):
        for y in range(y0, y1):
            life[x][y]=random.randint(0, 1)

#draw each cell
def drawcells():
    #draw cells
    for x in range(CELLWIDTH):
        for y in range(CELLHEIGHT):
            if life[x][y]==1:
                pygame.draw.rect(screen, twhcolors.BLACK, (x*CELLSIZE, y*CELLSIZE, CELLSIZE, CELLSIZE), 0)

#calculate new generation
#Any live cell with fewer than two live neighbors dies, as if by underpopulation.
#Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by overpopulation.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
def newgeneration():
    global generation
    generation+=1
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
                gen[x][y]=1
            if neighbors==3 and center==0:
                gen[x][y]=1
    for x in range(1, CELLWIDTH-1):
        for y in range(1, CELLHEIGHT-1):
            life[x][y]=gen[x][y]

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
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Conway Game Of Life')

# creates a clock
clock=pygame.time.Clock()

#create generation 0
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
    screen.fill(twhcolors.WHITE)

    #draw new generation
    twhwindow.drawgrid(screen, WIDTH, HEIGHT, CELLWIDTH, CELLHEIGHT, CELLSIZE, twhcolors.GRAY, 1)
    drawcells()
    newgeneration()
    twhwindow.drawinfobox(screen, myfont, WIDTH, HEIGHT, 220, 20, 5, 5, "Generation #"+str(generation), twhcolors.BLACK, twhcolors.WHITE, FILLSTYLE)

    #update display
    pygame.display.flip()

x=input("Done")
