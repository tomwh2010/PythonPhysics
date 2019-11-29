#Description
#Fullscreen game
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com
import pygame, sys
from pygame.locals import *

#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption('My name')
pygame.mouse.set_visible(False)

#draw background color to blank the screen
screen.fill(pygame.Color("gray69"))

# creates a clock
clock=pygame.time.Clock()

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 24)

#create text buffer
strBuffer="Click on ESC to exit"
#render buffer as picture
textsurface=myfont.render(strBuffer, 1, pygame.Color("black"))

#paint picture to screen at location 130,180
screen.blit(textsurface,(130, 180))

while True:
    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.mouse.set_visible(True)
            pygame.quit()
            sys.exit()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_ESCAPE]:
        pygame.mouse.set_visible(True)
        pygame.quit()
        sys.exit()

    #update display
    pygame.display.flip()
