##############################################################################
#Description
#Draw a message randomly with fading
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors
import random
import pygame.gfxdraw

##############################################################################
#constants
##############################################################################
#Frames pr second
FPS=5

WIDTH=600
HEIGHT=600

##############################################################################
#variables
##############################################################################
#create text buffer
strBuffer="Merry xmas!!!"
tree=pygame.image.load("tree.png")
counter=0

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
pygame.display.set_caption(strBuffer)

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 24)

#render buffer as picture
textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)

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

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #fade previous messages
    pygame.gfxdraw.box(screen, pygame.Rect(0,0,WIDTH,HEIGHT), (127,127,127,50))

    #calculate where to draw next
    x=random.randint(0,WIDTH-100)
    y=random.randint(0,HEIGHT-50)

    #draw the text
    screen.blit(textsurface,(x, y+150))

    #draw the tree
    screen.blit(tree, (x,y))

    #update display
    pygame.display.flip()
