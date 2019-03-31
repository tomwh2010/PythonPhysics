##############################################################################
#Description
#Animating pi by hitting a circle, inscribed in a square, with infinite number of darts
#PI is therefore defined as 4*num_hit_target/num_tries
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors
import twhwindow
from math import pi
import random
import twhsplash

twhsplash.splash("PI")

##############################################################################
#constants (variable names written with upper case)
##############################################################################
#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

#Frames pr second
FPS=360

#window size
WIDTH=600
HEIGHT=630
CENTER=WIDTH/2

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0
FRAMED=1

##############################################################################
#variables
##############################################################################
num_tries=1
errorstop=1E-10
num_hit_target=0
animate=False
error=0
MyPI=0

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
pygame.display.set_caption('PI calculation')

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 14)

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

#drawcircle and box
#circle(screen, color, coords(x, y), radius, fillstyle
pygame.draw.circle(screen, twhcolors.RED, (WIDTH//2, WIDTH//2), WIDTH//2, FILLED)
#rect(screen, color, coords(top, left, width, height), fillstyle
pygame.draw.rect(screen, twhcolors.BLACK, (0, 0, WIDTH, WIDTH), FRAMED)

# creates a clock
clock=pygame.time.Clock()

##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick()

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # if any key is pressed
        elif event.type==pygame.KEYDOWN:
            animate=True

    if animate:
        num_tries=num_tries+1
        x=random.random()*2-1
        y=random.random()*2-1
        test=x**2+y**2
        if test<=1:
            num_hit_target+=1
            MyPI=4*num_hit_target/num_tries
            error=abs(MyPI-pi)
        if error<errorstop:
            animate=False

        ballx=int(CENTER+CENTER*x)
        bally=int(CENTER+CENTER*y)
        #rect(screen, color, coords(top, left, width, height), fillstyle
        pygame.draw.rect(screen, twhcolors.BLACK, (ballx, bally, 2, 2), FILLED)

        #create text buffer
        strBuffer="PI="+str(MyPI)
        twhwindow.drawinfobox(screen, myfont, WIDTH, HEIGHT, WIDTH, 20, 0, 0, strBuffer, twhcolors.BLACK, twhcolors.SILVER, FILLSTYLE)
        strBuffer="Error="+str(error)
        twhwindow.drawinfobox(screen, myfont, WIDTH, HEIGHT, WIDTH-150, 20, 0, 0, strBuffer, twhcolors.BLACK, twhcolors.SILVER, FILLSTYLE)
        strBuffer="num_tries="+str(num_tries)
        twhwindow.drawinfobox(screen, myfont, WIDTH, HEIGHT, WIDTH-330, 20, 0, 0, strBuffer, twhcolors.BLACK, twhcolors.SILVER, FILLSTYLE)

    #update display
    pygame.display.flip()
