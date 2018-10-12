##############################################################################
#Description
#A simple game about a crane
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors

##############################################################################
#constants (variable names written with upper case)
##############################################################################
FPS=40 #Frames pr second

#window size
WIDTH=1200
HEIGHT=600

CRANE_Y0=478
CRANE_XOFFSET=81

FAR_LEFT=10
FAR_RIGHT=500

DELTA_CAR=10

DELTA_ARM=10
ARM_LOW=15
ARM_HIGH=65

DELTA_WIRE=5

##############################################################################
#variables
##############################################################################
cranearms=[[200, 45, 0, 0], [150, 90, 0, 0], [100, 135, 0, 0], [30, 0, 0, 0], [0, 0, 0, 0]] #radius, theta, x, y
car_left=FAR_LEFT

##############################################################################
#functions
##############################################################################
def drawinstructions():
    global screen

    strBuffer="Arm 1: Q: CCW W: CW"
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(949, 10))
    strBuffer="Arm 2: A: CCW S: CW"
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(949, 40))
    strBuffer="Arm 3: Z: CCW X: CW"
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(949, 70))
    strBuffer="Wire: E: Up R: Down"
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(949, 100))
    strBuffer="Clamp: D: On F: Off"
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(949, 130))
    strBuffer="Car: C: Left V: Right"
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(949, 160))

def drawvehicle():
    global screen
    #car
    pygame.draw.rect(screen, twhcolors.BLUE, (car_left, 500, 300, 80), 0)
    #cranehouse
    pygame.draw.rect(screen, twhcolors.RED, (car_left+10, 450, 150, 50), 0)
    #cockpit
    pointlist=[(car_left+210, 450), (car_left+210, 500), (car_left+300, 500)]
    pygame.draw.polygon(screen, twhcolors.GRAY, pointlist, 0)
    #wheels
    pygame.draw.circle(screen, twhcolors.BLACK, (car_left+40, 578), 20, 0)
    pygame.draw.circle(screen, twhcolors.BLACK, (car_left+240, 578), 20, 0)

def drawcrane():
    global cranearms, screen

    #draw arm 1
    pygame.draw.line(screen, twhcolors.BLACK, (car_left+CRANE_XOFFSET, CRANE_Y0), (cranearms[0][2], cranearms[0][3]), 5)

    #draw arm 2
    pygame.draw.line(screen, twhcolors.BLACK, (cranearms[0][2], cranearms[0][3]), (cranearms[1][2], cranearms[1][3]), 5)

    #draw arm 3
    pygame.draw.line(screen, twhcolors.BLACK, (cranearms[1][2], cranearms[1][3]), (cranearms[2][2], cranearms[2][3]), 5)

    #draw wire
    pygame.draw.line(screen, twhcolors.BLACK, (cranearms[2][2], cranearms[2][3]), (cranearms[3][2], cranearms[3][3]), 2)

    #draw magnetic clamp
    clampcolor=twhcolors.BLACK
    if cranearms[4][0]:
        clampcolor=twhcolors.RED
    pygame.draw.rect(screen, clampcolor, (cranearms[4][2], cranearms[4][3], 20, 20), 0)

def calculatexy(deltaarm1, deltaarm2, deltaarm3, deltawire, deltacar):
    global cranearms


    #if (cranearms[0][1]-DELTA_ARM)>=ARM_LOW:
    #    cranearms[0][1]-=DELTA_ARM
    #    cranearms[1][1]-=DELTA_ARM
    #    cranearms[2][1]-=DELTA_ARM

    #make a local copy
    localcranearms=[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(5):
        for j in range(4):
            localcranearms[i][j]=cranearms[i][j]
    #arm 1
    localcranearms[0][2]=car_left+CRANE_XOFFSET+int(localcranearms[0][0]*sin(radians(localcranearms[0][1])))
    localcranearms[0][3]=CRANE_Y0-int(localcranearms[0][0]*cos(radians(localcranearms[0][1])))

    #arm 2
    localcranearms[1][2]=localcranearms[0][2]+int(localcranearms[1][0]*sin(radians(localcranearms[1][1])))
    localcranearms[1][3]=localcranearms[0][3]-int(localcranearms[1][0]*cos(radians(localcranearms[1][1])))

    #arm 3
    localcranearms[2][2]=localcranearms[1][2]+int(localcranearms[2][0]*sin(radians(localcranearms[2][1])))
    localcranearms[2][3]=localcranearms[1][3]-int(localcranearms[2][0]*cos(radians(localcranearms[2][1])))

    #wire
    localcranearms[3][2]=localcranearms[2][2]
    localcranearms[3][3]=localcranearms[2][3]+localcranearms[3][0]

    #magnetic clamp
    localcranearms[4][2]=localcranearms[3][2]-10
    localcranearms[4][3]=localcranearms[3][3]-10

    #check if clamp is too low
    if (localcranearms[4][3]+20)>HEIGHT:
        print("We're too low, cancel move")
        return

    #we're good; copy back
    for i in range(5):
        for j in range(4):
            cranearms[i][j]=localcranearms[i][j]

def drawmousecoords():
    global screen
    #draw mouse position
    position=pygame.mouse.get_pos()
    strBuffer="Pos x: "+str(position[0])+" y: "+str(position[1])
    textsurface=myfont.render(strBuffer, 1, twhcolors.BLACK)
    screen.blit(textsurface,(WIDTH-180, HEIGHT-30))

def drawbox():
    global screen
    pygame.draw.rect(screen, twhcolors.YELLOW, (500, 548, 50, 50), 0)

##############################################################################
#initial code
##############################################################################
pygame.init() #initialize the pygame environment

# set up the window with size and caption
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Framework')

# creates a clock
clock=pygame.time.Clock()

# you have to call this at the start if you want to use this module.
pygame.font.init()

#choose font for later use
myfont=pygame.font.SysFont('Times New Roman', 24)

#initalize xy for each arm, wire and clamp
calculatexy()

##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill(twhcolors.SILVER)

    #get events from the event queue
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if any key is pressed
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                print("Arm1 CCW")
                calculatexy(-DELTA_ARM, -DELTA_ARM, -DELTA_ARM, 0, 0)
            elif event.key==pygame.K_w:
                print("Arm1 CW")
                calculatexy(DELTA_ARM, DELTA_ARM, DELTA_ARM, 0, 0)

            elif event.key==pygame.K_a:
                print("Arm2 CCW")
                calculatexy(0, -DELTA_ARM, -DELTA_ARM, 0, 0)
            elif event.key==pygame.K_s:
                print("Arm2 CW")
                calculatexy(0, DELTA_ARM, DELTA_ARM, 0, 0)

            elif event.key==pygame.K_z:
                print("Arm3 CCW")
                calculatexy(0, 0, -DELTA_ARM, 0, 0)
            elif event.key==pygame.K_x:
                print("Arm3 CW")
                calculatexy(0, 0, DELTA_ARM, 0, 0)

            elif event.key==pygame.K_e:
                print("Wire up")
                calculatexy(0, 0, 0, -DELTA_WIRE, 0)
                if (cranearms[3][0]-DELTA_WIRE)>=DELTA_WIRE:
                    cranearms[3][0]-=DELTA_WIRE
            elif event.key==pygame.K_r:
                print("Wire down")
                calculatexy(0, 0, 0, DELTA_WIRE, 0)

            elif event.key==pygame.K_d:
                print("Clamp on")
                cranearms[4][0]=1
            elif event.key==pygame.K_f:
                print("Clamp off")
                cranearms[4][0]=0

            #move car left or right
            elif event.key==pygame.K_c:
                calculatexy(0, 0, 0, 0, -DELTA_CAR)
            elif event.key==pygame.K_v:
                calculatexy(0, 0, 0, 0, DELTA_CAR)

    calculatexy()
    drawcrane()
    drawvehicle()
    drawinstructions()
    drawmousecoords()

    #update display
    pygame.display.flip()

"""
elif event.type==pygame.KEYDOWN:
    if event.key==pygame.K_q:
        print("Arm1 CCW")
        calculatexy(-DELTA_ARM, -DELTA_ARM, -DELTA_ARM, 0, 0, 0)
    elif event.key==pygame.K_w:
        print("Arm1 CW")
        calculatexy(DELTA_ARM, DELTA_ARM, DELTA_ARM, 0, 0, 0)

    elif event.key==pygame.K_a:
        print("Arm2 CCW")
        calculatexy(0, -DELTA_ARM, -DELTA_ARM, 0, 0, 0)
        if (cranearms[1][1]-DELTA_ARM)>=(cranearms[0][1]+ARM_LOW):
            cranearms[1][1]-=DELTA_ARM
            cranearms[2][1]-=DELTA_ARM
    elif event.key==pygame.K_s:
        print("Arm2 CW")
        calculatexy(0, DELTA_ARM, DELTA_ARM, 0, 0, 0)
        if (cranearms[1][1]+DELTA_ARM)<=(cranearms[0][1]+ARM_HIGH):
            cranearms[1][1]+=DELTA_ARM
            cranearms[2][1]+=DELTA_ARM

    elif event.key==pygame.K_z:
        print("Arm3 CCW")
        if (cranearms[2][1]-DELTA_ARM)>=(cranearms[1][1]+ARM_LOW):
            cranearms[2][1]-=DELTA_ARM
    elif event.key==pygame.K_x:
        print("Arm3 CW")
        if (cranearms[2][1]+DELTA_ARM)<=(cranearms[1][1]+ARM_HIGH):
            cranearms[2][1]+=DELTA_ARM

    elif event.key==pygame.K_e:
        print("Wire up")
        if (cranearms[3][0]-DELTA_WIRE)>=DELTA_WIRE:
            cranearms[3][0]-=DELTA_WIRE
    elif event.key==pygame.K_r:
        print("Wire down")
        if (cranearms[3][0]+DELTA_WIRE)<=50:
            cranearms[3][0]+=DELTA_WIRE

    elif event.key==pygame.K_d:
        print("Clamp on")
        cranearms[4][0]=1
    elif event.key==pygame.K_f:
        print("Clamp off")
        cranearms[4][0]=0
"""
