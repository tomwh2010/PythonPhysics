#Description
#Draw a simple blinking string
import pygame, sys
from pygame.locals import *

#Frames pr second
FPS=24

#window size
WIDTH=400
HEIGHT=400

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Blink my name')

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

#status flag to show text or not
blinkit=False

#when to blink
nCycles=0
maxCycles=12 #12 gives about every half second

while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    #I paint the background here instead to blank the screen for each frame
    screen.fill(pygame.Color("gray69"))

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    #increase nCycles
    nCycles+=1

    #if we've reached maximum then its time to switch state
    if nCycles==maxCycles:
        #reset counter
        nCycles=0

        #switch state
        blinkit=not blinkit

    #if blinkit is true then show name
    if blinkit:
        #paint picture to screen at location 130,180
        screen.blit(textsurface,(130, 180))

    #update display
    pygame.display.flip()
