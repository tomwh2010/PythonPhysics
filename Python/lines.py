#Description
#Animation with lines
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *
from twhcolors import *

#line thickness
LINESTYLE=2

#Frames pr second
FPS=24

#window size
WIDTH=600
HEIGHT=600

#delta x, y for each update
DELTA=10

#initial start, end point for line
x_start=0
y_start=300
x_stop=300
y_stop=0

#initial delta for start, stop
dx_start=0
dy_start=-DELTA
dx_stop=DELTA
dy_stop=0

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Lines')

#draw background color to blank the screen
screen.fill(pygame.Color("black"))

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

    #line(screen, color, coords1(x, y), coords2(x, y), fillstyle
    pygame.draw.line(screen, getColor(), (x_start, y_start), (x_stop, y_stop), LINESTYLE)

    #next color in the list
    cyclecolor()

    #change deltas if hitting one of the four corners
    if x_start==0 and y_start==0:
        dx_start=DELTA
        dy_start=0
        dx_stop=0
        dy_stop=DELTA

    if x_start==HEIGHT and y_start==0:
        dx_start=0
        dy_start=DELTA
        dx_stop=-DELTA
        dy_stop=0

    if x_start==HEIGHT and y_start==HEIGHT:
        dx_start=-DELTA
        dy_start=0
        dx_stop=0
        dy_stop=-DELTA

    if x_start==0 and y_start==HEIGHT:
        dx_start=0
        dy_start=-DELTA
        dx_stop=DELTA
        dy_stop=0

    #update start, end points
    x_start+=dx_start
    y_start+=dy_start
    x_stop+=dx_stop
    y_stop+=dy_stop

    #update display
    pygame.display.flip()
