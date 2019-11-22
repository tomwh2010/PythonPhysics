#Description
#Different window routines
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame

#draw a grid to screen; see conway.py for usage
def drawgrid(screen, width, height, columns, rows, size, gridcolor, linewidth):
    #horizontal lines
    for i in range(columns):
        pygame.draw.line(screen, gridcolor, (0, i*size), (width, i*size), linewidth)

    #vertical lines
    for i in range(rows):
        pygame.draw.line(screen, gridcolor, (i*size, 0), (i*size, height), linewidth)

#TODO make it generic with placement: top bottom, left center right
def drawinfobox(screen, font, windowwidth, windowheight, boxwidth, boxheight, textoffsetx, textoffsety, string, foregroundcolor, backgroundcolor, fillstyle):
    #draw background
    pygame.draw.rect(screen, backgroundcolor, (windowwidth-boxwidth, windowheight-boxheight, boxwidth, boxheight), fillstyle)
    #render buffer as picture
    textsurface=font.render(string, 1, foregroundcolor)
    #paint picture to screen
    screen.blit(textsurface, (windowwidth-boxwidth+textoffsetx, windowheight-boxheight+textoffsety))
    