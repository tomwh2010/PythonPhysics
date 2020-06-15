
#Description
#Move a ball around with UP/DOWN/LEFT/RIGHT continuously
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

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 24)

#create text buffer
strBuffer="Move cursor with arrow keys"

#render buffer as picture
textsurface=myfont.render(strBuffer, 1, pygame.Color("black"))

# creates a clock
clock=pygame.time.Clock()

#initial location of the ball; center
myball=[WIDTH//2, HEIGHT//2]

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #by using this construct instead of event we will get
    #continous flow + at 45 degree angles if we want to to
    keys_pressed = pygame.key.get_pressed()

    if keys_pressed[K_LEFT]:
        myball[0]-=5

    if keys_pressed[K_RIGHT]:
        myball[0]+=5

    if keys_pressed[K_UP]:
        myball[1]-=5

    if keys_pressed[K_DOWN]:
        myball[1]+=5

    #draw background color to blank the screen
    screen.fill(pygame.Color("gray69"))

    #paint picture to screen at location 130,180
    screen.blit(textsurface,(10, 10))

    #circle(screen, color, coords(x,y), radius, fillstyle
    pygame.draw.circle(screen, SHAPE_COLOR, myball, 10, FILLSTYLE)

    #update display
    pygame.display.flip()
