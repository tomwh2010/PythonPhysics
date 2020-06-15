#Description
#Animation with objects that fades to the background
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *
import random
import pygame.gfxdraw #important if fading is required

#Frames pr second
FPS=24

#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLED=0

#window size
WIDTH=700
HEIGHT=700

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tutti Frutti Fade')

# creates a clock
clock=pygame.time.Clock()

#draw background color to blank the screen
screen.fill((192,192,192)) #gray background

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #add white smoke to entire screen
    #the fourth, optional, part of a color tuple  is the alpha channel
    #or how see-thru it is.
    #https://en.wikipedia.org/wiki/Alpha_compositing
    #therefore -> in this example the higher it is the faster it will fade
    pygame.gfxdraw.box(screen, pygame.Rect(0,0,WIDTH,HEIGHT), (255,255,255,5))

    #calculate random type, r, g, b, x, y and size
    R=random.randint(0, 255)
    G=random.randint(0, 255)
    B=random.randint(0, 255)
    x=random.randint(0, WIDTH)
    y=random.randint(0, HEIGHT)
    width=random.randint(8, 40)
    height=random.randint(8, 40)
    circlerectangle=random.randint(0,2)
    if circlerectangle==2:
        pygame.draw.circle(screen, (R,G,B), (x, y), width, FILLED)
    elif circlerectangle==1:
        pygame.draw.ellipse(screen, (R,G,B), (x, y, width, height), FILLED)
    else:
        pygame.draw.rect(screen, (R,G,B), (x, y, width, height), FILLED)

    #update display
    pygame.display.flip()
