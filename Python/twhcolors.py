#Description
#Predefined color values and color cycling functions
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame

# set up the color variables
BLACK   = pygame.Color("black")
BLUE    = pygame.Color("blue")
CYAN    = pygame.Color("cyan")
GRAY    = pygame.Color("gray69")
GREEN   = pygame.Color("green")
LIME    = pygame.Color("limegreen")
MAGENTA = pygame.Color("magenta")
MAROON  = pygame.Color("maroon")
NAVY    = pygame.Color("navy")
OLIVE   = pygame.Color("olivedrab")
PINK    = pygame.Color("pink")
PURPLE  = pygame.Color("purple")
RED     = pygame.Color("red")
SILVER  = pygame.Color("gray69")
TEAL    = pygame.Color("springgreen3")
YELLOW  = pygame.Color("yellow")
WHITE   = pygame.Color("white")

#one type of colorcycle
COLORCYCLE=[WHITE, RED, GREEN, BLUE, GRAY, SILVER, YELLOW, CYAN, MAGENTA, PINK]

#current color index
colorindex=0

#cycle to the next color
def cyclecolor():
    global colorindex
    colorindex+=1
    if colorindex==len(COLORCYCLE)-1:
        colorindex=0

def getColor():
    return COLORCYCLE[colorindex]
