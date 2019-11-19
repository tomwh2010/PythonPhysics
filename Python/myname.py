#Description
#Draw a simple string

import pygame, sys
from pygame.locals import *

#Frames pr second
FPS=40

#window size
WIDTH=400
HEIGHT=400

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

#draw background color to blank the screen
screen.fill(pygame.Color("gray69"))

# creates a clock
clock=pygame.time.Clock()

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 24)

#create text buffer
strBuffer="My name is Tom"
#render buffer as picture
textsurface=myfont.render(strBuffer, 1, pygame.Color("black"))

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #paint picture to screen at location 130,180
    screen.blit(textsurface,(130, 180))

    #update display
    pygame.display.flip()
