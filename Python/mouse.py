#Description
#Mouseclick on a square; change color according to state
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0

#Frames pr second
FPS=25

#window size
WIDTH=600
HEIGHT=620

#chosen state
chosen=False

#box location and dimensions
box=pygame.Rect(100, 100, 300, 300)

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mouse')

#draw background color to blank the screen
screen.fill(pygame.Color("gray69"))

# creates a clock
clock=pygame.time.Clock()

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit
        #do we have collision, do we hove the mouse over the box
        elif event.type == MOUSEMOTION:
            collision=False
            x,y=event.pos
            if box.collidepoint(x, y):
                collision=True
        #if user clicked on the square->change state
        elif event.type == MOUSEBUTTONUP:
            if collision:
                chosen=not chosen

    #check state and collision
    if chosen:
        if collision:
            color=pygame.Color("green")
        else:
            color=color=pygame.Color("blue")
    else:
        if collision:
            color=color=pygame.Color("red")
        else:
            color=color=pygame.Color("yellow")

    pygame.draw.rect(screen, color, box, FILLED)

    #update display
    pygame.display.flip()
