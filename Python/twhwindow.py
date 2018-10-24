##############################################################################
#Description
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame

##############################################################################
#constants
##############################################################################
#WIDTH=600
#HEIGHT=600
#CELLSIZE=10

#assert WIDTH%CELLSIZE==0, "Wrong width, cellsize"
#assert HEIGHT%CELLSIZE==0, "Wrong height, cellsize"

#CELLWIDTH=WIDTH//CELLSIZE
#CELLHEIGHT=HEIGHT//CELLSIZE

##############################################################################
#variables
##############################################################################
#windowwidth=600
#windowheight=600
#cellsize=10

##############################################################################
#functions
##############################################################################
def drawgrid2(screen):
    #horizontal lines
    for i in range(CELLWIDTH):
        pygame.draw.line(screen, twhcolors.GRAY, (0, i*CELLSIZE), (WIDTH, i*CELLSIZE), 1)

    #vertical lines
    for i in range(CELLHEIGHT):
        pygame.draw.line(screen, twhcolors.GRAY, (i*CELLSIZE, 0), (i*CELLSIZE, HEIGHT), 1)

def drawinfobox(screen, windowwidth, windowheight, boxwidth, boxheight, textoffsetx, textoffsety, string, foregroundcolor, backgroundcolor, fillstyle):
    #draw background
    pygame.draw.rect(screen, backgroundcolor, (windowwidth-boxwidth, windowheight-boxheight, boxwidth, boxheight), fillstyle)
    #render buffer as picture
    textsurface=myfont.render(string, 1, foregroundcolor)
    #paint picture to screen
    screen.blit(textsurface, (windowwidth-boxwidth+textoffsetx, windowheight-boxheight+textoffsety))

##############################################################################
#initial code
##############################################################################

##############################################################################
#main loop
##############################################################################
