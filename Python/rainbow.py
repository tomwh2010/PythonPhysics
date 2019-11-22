#Draw a rainbow
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *

#define the different colors
GRAY=pygame.Color("gray69")
RED = pygame.Color("red")
ORANGE=pygame.Color("orange")
YELLOW=pygame.Color("yellow")
GREEN=pygame.Color("green")
BLUE=pygame.Color("blue")
INDIGO=(75,0,130)#pygame.Color("indigo")
VIOLET=pygame.Color("magenta4")

#setup the rainbow colors from outer to inner
RAINBOW=[RED, ORANGE, YELLOW, GREEN, BLUE, INDIGO, VIOLET, GRAY]

#Frames pr second
FPS=24

#window size
WIDTH=400
HEIGHT=200

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rainbow')

#draw background color to blank the screen
screen.fill(GRAY)

# creates a clock
clock=pygame.time.Clock()

#draw only once in the main loop
running=True

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #if we're up and running
    if running:
        size=200
        #draw circles with decreasing circles
        #if the last circles color is the same as the background then
        #we have a nice rainbow
        for i in range(8):
            pygame.draw.circle(screen, RAINBOW[i], (WIDTH//2,HEIGHT), size)
            size-=20
        
    running=False

    #update display
    pygame.display.flip()
