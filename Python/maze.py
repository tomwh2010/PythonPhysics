##############################################################################
#Description
#Drawing a maze
#Bits
#0000 0001 Up
#0000 0010 right
#0000 0100 down
#0000 1000 left
#0001 0000 start
#0010 0000 stop
#0100 0000 mark
#1000 0000 robot
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors
import twhwindow

##############################################################################
#constants (variable names written with upper case)
##############################################################################
THINLINE=1
THICKLINE=2
BACKGROUNDCOLOR=twhcolors.SILVER
THINLINECOLOR=twhcolors.RED
THICKLINECOLOR=twhcolors.BLACK

#Frames pr second
FPS=40

#window size
WIDTH=700
HEIGHT=700
OFFSETX=10
OFFSETY=10
CELLSIZEX=100
CELLSIZEY=100
CELLNUMX=6
CELLNUMY=4

assert (WIDTH-OFFSETX-CELLSIZEX*CELLNUMX)>0, "Width too narrow"
assert (HEIGHT-OFFSETY-CELLSIZEY*CELLNUMY)>0, "Height too narrow"

##############################################################################
#variables
##############################################################################
maze=[[9, 5, 5, 3, 9, 39], [12, 5, 3, 12, 2, 11], [9, 3, 8, 3, 10, 10], [30, 12, 6, 14, 12, 6]]
print(maze)

##############################################################################
#functions
##############################################################################
def printmaze():
    for y in range(CELLNUMY):
        for x in range(CELLNUMX):
            #draw up
            x0=x*100+OFFSETX
            y0=y*100+OFFSETY
            x1=(x+1)*100+OFFSETX
            y1=y*100+OFFSETY
            color=THINLINECOLOR
            linestyle=THINLINE

            if maze[y][x]&1==1:
                color=THICKLINECOLOR
                linestyle=THICKLINE
                pygame.draw.line(screen, color, (x0, y0), (x1, y1), linestyle)
            else:
                twhwindow.drawdashedline(screen, THINLINECOLOR, linestyle, x0, y0, x1, y1, 5)

            #draw right
            x0=(x+1)*100+OFFSETX
            y1=(y+1)*100+OFFSETY
            color=THINLINECOLOR
            linestyle=THINLINE
            if maze[y][x]&2==2:
                color=THICKLINECOLOR
                linestyle=THICKLINE
            pygame.draw.line(screen, color, (x0, y0), (x1, y1), linestyle)

            #draw down
            x0=x*100+OFFSETX
            y0=(y+1)*100+OFFSETY
            color=THINLINECOLOR
            linestyle=THINLINE
            if maze[y][x]&4==4:
                color=THICKLINECOLOR
                linestyle=THICKLINE
            pygame.draw.line(screen, color, (x0, y0), (x1, y1), linestyle)

            #draw left
            y0=y*100+OFFSETY
            x1=x*100+OFFSETX
            color=THINLINECOLOR
            linestyle=THINLINE
            if maze[y][x]&8==8:
                color=THICKLINECOLOR
                linestyle=THICKLINE
            pygame.draw.line(screen, color, (x0, y0), (x1, y1), linestyle)

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Maze')

# creates a clock
clock=pygame.time.Clock()

##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill(BACKGROUNDCOLOR)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    printmaze()
    #update display
    pygame.display.flip()
