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
import twhsplash

twhsplash.splash("SimonSays")

##############################################################################
#constants
##############################################################################
#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0
FRAMED=4

#Frames pr second
FPS=40

#window size
WIDTH=600
HEIGHT=620

##############################################################################
#variables
##############################################################################
chosen=False
index=-1
stop=1
boxes=[]
boxes.append(pygame.Rect(  0,   0, 300, 300))
boxes.append(pygame.Rect(300,   0, 300, 300))
boxes.append(pygame.Rect(  0, 300, 300, 300))
boxes.append(pygame.Rect(300, 300, 300, 300))
sequence=[0,3,1,2,0,0,1,3,2,1,2,3]

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

    x,y=pygame.mouse.get_pos()
    index=-1
    for i in range(4):
        if boxes[i].collidepoint(x, y):
            index=i

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            if index>-1:
                chosen=not chosen

    #rect(screen, color, coords(top, left, width, height), fillstyle
    pygame.draw.rect(screen, twhcolors.RED,    boxes[0], FILLED)
    pygame.draw.rect(screen, twhcolors.BLUE,   boxes[1], FILLED)
    pygame.draw.rect(screen, twhcolors.GREEN,  boxes[2], FILLED)
    pygame.draw.rect(screen, twhcolors.YELLOW, boxes[3], FILLED)
    if index>-1:
        pygame.draw.rect(screen, twhcolors.BLACK,  boxes[index], FRAMED)

    #update display
    pygame.display.flip()
