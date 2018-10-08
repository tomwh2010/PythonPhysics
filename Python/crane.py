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
cranearms=[[200, 45], [150, 90], [100, 135], [30]] #radius, theta
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
    crane_x1=car_left+CRANE_XOFFSET+int(cranearms[0][0]*sin(radians(cranearms[0][1])))
    crane_y1=CRANE_Y0-int(cranearms[0][0]*cos(radians(cranearms[0][1])))
    pygame.draw.line(screen, twhcolors.BLACK, (car_left+CRANE_XOFFSET, CRANE_Y0), (crane_x1, crane_y1), 5)

    #draw arm 2
    crane_x2=crane_x1+int(cranearms[1][0]*sin(radians(cranearms[1][1])))
    crane_y2=crane_y1-int(cranearms[1][0]*cos(radians(cranearms[1][1])))
    pygame.draw.line(screen, twhcolors.BLACK, (crane_x1, crane_y1), (crane_x2, crane_y2), 5)

    #draw arm 3
    crane_x3=crane_x2+int(cranearms[2][0]*sin(radians(cranearms[2][1])))
    crane_y3=crane_y2-int(cranearms[2][0]*cos(radians(cranearms[2][1])))
    pygame.draw.line(screen, twhcolors.BLACK, (crane_x2, crane_y2), (crane_x3, crane_y3), 5)

    #draw wire
    crane_x4=crane_x3
    crane_y4=crane_y3+cranearms[3][0]
    pygame.draw.line(screen, twhcolors.BLACK, (crane_x3, crane_y3), (crane_x4, crane_y4), 2)

    #draw magnetic clamp
    clamp_left=crane_x4-10
    clamp_top=crane_y4-10
    clamp_width=20
    clamp_height=20
    pygame.draw.rect(screen, twhcolors.RED, (clamp_left, clamp_top, clamp_width, clamp_height), 0)

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
                if (cranearms[0][1]-DELTA_ARM)>=ARM_LOW:
                    cranearms[0][1]-=DELTA_ARM
                    cranearms[1][1]-=DELTA_ARM
                    cranearms[2][1]-=DELTA_ARM
            elif event.key==pygame.K_w:
                print("Arm1 CW")
                if (cranearms[0][1]+DELTA_ARM)<=ARM_HIGH:
                    cranearms[0][1]+=DELTA_ARM
                    cranearms[1][1]+=DELTA_ARM
                    cranearms[2][1]+=DELTA_ARM

            elif event.key==pygame.K_a:
                print("Arm2 CCW")
                if (cranearms[1][1]-DELTA_ARM)>=(cranearms[0][1]+ARM_LOW):
                    cranearms[1][1]-=DELTA_ARM
                    cranearms[2][1]-=DELTA_ARM
            elif event.key==pygame.K_s:
                print("Arm2 CW")
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
            elif event.key==pygame.K_f:
                print("Clamp off")

            #move car left or right
            elif event.key==pygame.K_c:
                car_left-=DELTA_CAR
                if car_left<FAR_LEFT:
                    car_left=FAR_LEFT
            elif event.key==pygame.K_v:
                car_left+=DELTA_CAR
                if car_left>FAR_RIGHT:
                    car_left=FAR_RIGHT

            print(cranearms[0][1], cranearms[1][1], cranearms[2][1])

    drawcrane()
    drawvehicle()
    drawinstructions()


    #update display
    pygame.display.flip()
