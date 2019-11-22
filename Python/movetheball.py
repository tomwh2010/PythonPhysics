
#Description
#Move a ball around with UP/DOWN/LEFT/RIGHT once pr click
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
WIDTH=800
HEIGHT=500

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Move a ball')

# creates a clock
clock=pygame.time.Clock()

#initial location of the ball; center
myball=[WIDTH//2, HEIGHT//2]

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

        # if any key is pressed
        elif event.type==pygame.KEYDOWN:
            # if the 'up' key is pressed
            if event.key==pygame.K_UP:
                # moves the blue circle 10 pixels up
                myball[1]-=10

            # if the 'down' key is pressed
            elif event.key==pygame.K_DOWN:
                # moves the blue circle 10 pixels down
                myball[1]+=10

            # if the 'left' key is pressed
            elif event.key==pygame.K_LEFT:
                # moves the blue circle 10 pixels to the left
                myball[0]-=10

            # if the 'right' key is pressed
            elif event.key==pygame.K_RIGHT:
                # moves the blue circle 10 pixels to the right
                myball[0]+=10

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, myball, 10, FILLSTYLE)

    #update display
    pygame.display.flip()
