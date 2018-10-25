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

##############################################################################
#variables
##############################################################################

##############################################################################
#functions
##############################################################################
def drawgrid(screen, width, height, columns, rows, size, gridcolor):
    #horizontal lines
    for i in range(columns):
        pygame.draw.line(screen, gridcolor, (0, i*size), (width, i*size), 1)

    #vertical lines
    for i in range(rows):
        pygame.draw.line(screen, gridcolor, (i*size, 0), (i*size, height), 1)

#TODO make it generic with placement: top bottom, left center right
def drawinfobox(screen, font, windowwidth, windowheight, boxwidth, boxheight, textoffsetx, textoffsety, string, foregroundcolor, backgroundcolor, fillstyle):
    #draw background
    pygame.draw.rect(screen, backgroundcolor, (windowwidth-boxwidth, windowheight-boxheight, boxwidth, boxheight), fillstyle)
    #render buffer as picture
    textsurface=font.render(string, 1, foregroundcolor)
    #paint picture to screen
    screen.blit(textsurface, (windowwidth-boxwidth+textoffsetx, windowheight-boxheight+textoffsety))

##############################################################################
#initial code
##############################################################################

##############################################################################
#main loop
##############################################################################
