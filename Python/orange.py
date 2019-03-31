#catch the orange man
import pygame, sys
from pygame.locals import *
import twhcolors
import random
from math import sqrt
fps=1
maxupdate=2000
update=0

file="fakenews1.wav"
pygame.mixer.init()
pygame.mixer.music.load(file)

WIDTH=600
HEIGHT=600

trump=pygame.image.load("trump.png")
box=pygame.Rect(0,0,83,112)

score=0
chosen=False

pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Trump")

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            collision=False
            x,y=event.pos
            if box.collidepoint(x, y):
                collision=True
        #if user clicked on the square->change state
        elif event.type == MOUSEBUTTONUP:
            if collision:
                pygame.mixer.music.play()
                score+=1
                pygame.display.set_caption("Catch the Trump Score: "+str(score))
                maxupdate=int(maxupdate*0.96)
                print(score, maxupdate)

    #draw background color to blank the screen
    screen.fill(twhcolors.SILVER)

    update+=1
    if update>=maxupdate:
        update=0
        #calculate where to draw next
        x=random.randint(0, WIDTH-box.width)
        y=random.randint(0, HEIGHT-box.height)
        box.left=x
        box.top=y

        #draw the tree
        screen.blit(trump, (x,y))

        #update display
        pygame.display.flip()
