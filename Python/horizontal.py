#Description
#Ball moves horizontal
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *

#color of the ball
SHAPE_COLOR=pygame.Color("red")

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0

#Frames pr second
FPS=40

#window size
WIDTH=600
HEIGHT=600

#size of the ball
BALLSIZE=10

#how close to edge before bouncing
BOUNCEDISTANCE=8

#delta for ball on each update
DELTA=5

#current delta
delta_x=DELTA

#initial location of ball
myball=[BOUNCEDISTANCE, HEIGHT//2]

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

# creates a clock
clock=pygame.time.Clock()

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill(pygame.Color("gray69"))

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, myball, BALLSIZE, FILLSTYLE)

    #update position
    myball[0]+=delta_x

    #if ball hits right side; change delta
    if myball[0]>=(WIDTH-BOUNCEDISTANCE):
        delta_x=-DELTA

    #if ball hits left side; change delta
    if myball[0]<=BOUNCEDISTANCE:
        delta_x=DELTA

    #update display
    pygame.display.flip()
