##############################################################################
#Description
#2048 game
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
import twhcolors
import twhwindow
import random

random.seed(0)

##############################################################################
#constants
##############################################################################
#style=0 => filled, style=1 => thin line, style=4 => thick line
FILLSTYLE=0
LINESTYLE=4

FPS=4 #Frames pr second

#window size
WIDTH=400
HEIGHT=400
CELLSIZE=100

assert WIDTH%CELLSIZE==0, "Wrong width, cellsize"
assert HEIGHT%CELLSIZE==0, "Wrong height, cellsize"

CELLWIDTH=WIDTH//CELLSIZE
CELLHEIGHT=HEIGHT//CELLSIZE

##############################################################################
#variables
##############################################################################
#create 4x4 list
gamenum=[[0 for x in range(4)] for y in range(4)]
##############################################################################
#functions
##############################################################################
def addnumber(n):
    iteration=0
    tries=0
    while tries<32:
        tries+=1
        row=random.randint(0, 3)
        column=random.randint(0, 3)
        if gamenum[row][column]==0:
            gamenum[row][column]=2
            print("Added number at(",row,",",column,")")
            iteration+=1
        if iteration==n:
            print("Done adding number")
            break
    else:
        print("No more empty cells")

def printasciigame():
    print()
    for row in range(4):
        print(gamenum[row])


#0=>right
#1=>down
#2=>left
#3=>up
def move(direction):
    #up/left
    start_i=0
    stop_i=3
    step_i=1
    start_j=1
    stop_j=4
    step_j=1

    if direction<2:
        #down/right
        start_i=3
        stop_i=0
        step_i=-1
        start_j=-1
        stop_j=-1
        step_j=-1

    #scroll thru the cells right
    for h in range(4):
        for i in range(start_i, stop_i, step_i):
            for j in range(i+start_j, stop_j, step_j):
                if direction%2==0:
                    #convert from 2->4 etc
                    if gamenum[h][i]>0 and gamenum[h][i]==gamenum[h][j]:
                        gamenum[h][i]+=gamenum[h][j]
                        gamenum[h][j]=0
                    #trickle right/down
                    if gamenum[h][i]==0 and gamenum[h][j]>0:
                        gamenum[h][i]=gamenum[h][j]
                        gamenum[h][j]=0
                else:
                    #convert from 2->4 etc
                    if gamenum[i][h]>0 and gamenum[i][h]==gamenum[j][h]:
                        gamenum[i][h]+=gamenum[j][h]
                        gamenum[j][h]=0
                    #trickle up/left
                    if gamenum[i][h]==0 and gamenum[j][h]>0:
                        gamenum[i][h]=gamenum[j][h]
                        gamenum[j][h]=0

def drawnums():
    for row in range(4):
        for column in range(4):
            if gamenum[row][column]>0:
                buffer=str(gamenum[row][column])
                textsurface=myfont.render(buffer, 1, twhcolors.BLACK)
                #paint picture to screen
                screen.blit(textsurface, (column*CELLSIZE+2, row*CELLSIZE+2))

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment
pygame.font.init() # you have to call this at the start if you want to use this module.

#choose font for later use
myfont = pygame.font.SysFont('Courier', 48)

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')

# creates a clock
clock=pygame.time.Clock()
#print initial matrix
printasciigame()
#add 2 numbers to start with
addnumber(2)
#print matrix
printasciigame()
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
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                move(3)
                addnumber(1)
                print("K_UP")
            elif event.key==pygame.K_RIGHT:
                move(0)
                addnumber(1)
                print("K_RIGHT")
            elif event.key==pygame.K_DOWN:
                move(1)
                addnumber(1)
                print("K_DOWN")
            elif event.key==pygame.K_LEFT:
                move(2)
                addnumber(1)
                print("K_LEFT")

            printasciigame()
    #draw background color to blank the screen
    screen.fill(twhcolors.WHITE)
    twhwindow.drawgrid(screen, WIDTH, HEIGHT, CELLWIDTH, CELLHEIGHT, CELLSIZE, twhcolors.GRAY, 1)
    drawnums()
    #update display
    pygame.display.flip()
