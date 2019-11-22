#Description
#Displaying different type of objects
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0
FRAMED=1
LINESTYLE=4

#Frames pr second
FPS=24

#window size
WIDTH=800
HEIGHT=500

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Objects')

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
            sys.exit()

    #circle(screen, color, coords(x, y), radius, fillstyle
    pygame.draw.circle(screen, pygame.Color("red"), (405, 405), 40, FILLED)

    #rect(screen, color, coords(top, left, width, height), fillstyle
    pygame.draw.rect(screen, pygame.Color("yellow"), (125, 225, 100, 100), FILLED)

    #ellipse(screen, color, coords(top, left, bottom, right), fillstyle
    pygame.draw.ellipse(screen, pygame.Color("blue"), (325, 25, 450, 100), FRAMED)

    #polygon(screen, color, pointlist((x, y)...), fillstyle
    pointlist_1 = [(25, 25), (105, 185), (185, 25)]
    pygame.draw.polygon(screen, pygame.Color("green"), pointlist_1, FRAMED)

    #line(screen, color, coords1(x, y), coords2(x, y), fillstyle
    pygame.draw.line(screen, pygame.Color("magenta"), (25, 200), (375, 200), LINESTYLE)

    #update display
    pygame.display.flip()
