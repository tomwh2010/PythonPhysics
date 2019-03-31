#sourcecode inspired by http://www.pygame.org/project-Splash+screen-1186-.html
import pygame
import time
import os, sys
import twhcolors
import pygame.gfxdraw

def splash(AppName="Test"):
    width=520
    height=292
    pic=pygame.image.load("74976727.png")
    print('Splash load...')
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((width,height),pygame.NOFRAME)
    background = pygame.Surface(screen.get_size())

    onoff=True
    seconds=5
    sec=0

    while sec<seconds:
        background.fill(twhcolors.SILVER)
        screen.blit(background, (0,0))
        screen.blit(pic, (0,0))
        pygame.gfxdraw.box(screen, pygame.Rect(0,0,width,height), (255,255,255,184))
        screen.blit(pygame.font.SysFont('Times New Roman', 48).render('tomwh2010 productions', 1, twhcolors.BLACK), (30,10))
        screen.blit(pygame.font.SysFont('Times New Roman', 48).render('proudly presents', 1, twhcolors.BLACK), (30,60))
        screen.blit(pygame.font.SysFont('Times New Roman', 48).render(AppName, 1, twhcolors.BLACK), (30,140))
        if onoff:
            screen.blit(pygame.font.SysFont('Times New Roman', 48).render('loading...', 1, twhcolors.BLACK), (178,220))
        onoff=not onoff
        pygame.display.update()
        time.sleep(1)
        sec+=1

#for development testing
if __name__ == "__main__":
    splash()
