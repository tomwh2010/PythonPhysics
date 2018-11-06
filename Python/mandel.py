##############################################################################
#Description
#Generating mandelbrot Fractal
#Inspired by https://gist.github.com/rameshvarun/5694091
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors

##############################################################################
#constants (variable names written with upper case)
##############################################################################
#Frames pr second
FPS=40

#window size
WIDTH=800
HEIGHT=600

##############################################################################
#variables
##############################################################################
max_iteration = 255
buffer=[[0.0 for x in range(WIDTH+1)] for y in range(HEIGHT+1)]

##############################################################################
#functions
##############################################################################
def calculate():
    global buffer, WIDTH, HEIGHT, max_iteration
    for i in range(WIDTH):
        if i%10==0:
            print(i*100//WIDTH,"%")
        for j in range(HEIGHT):
            x0=(float(i)/WIDTH)*3.5-2.5
            y0=(float(j)/HEIGHT)*2-1
            x=0
            y=0
            iteration=0

            while x*x+y*y<2*2 and iteration<max_iteration:
                xtemp=x*x-y*y+x0
                y=2*x*y+y0
                x=xtemp
                iteration=iteration+1

            buffer[j][i]=iteration

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment
pygame.init()

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mandelbrot Fractal')

#draw background color to blank the screen
screen.fill(twhcolors.SILVER)

# creates a clock
clock=pygame.time.Clock()

calculate()
##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            pygame.draw.rect(screen, (buffer[y][x],buffer[y][x],buffer[y][x]), (x, y, 1, 1), 0)
    #update display
    pygame.display.flip()

print("done")
