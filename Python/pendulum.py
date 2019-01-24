##############################################################################
#Description
#Pendulum
##############################################################################

##############################################################################
#libraries
##############################################################################
import pygame, sys
from pygame.locals import *
from math import *
import twhcolors
import pygame.gfxdraw
import random

pygame.init()
##############################################################################
#constants
##############################################################################
#Frames pr second
FPS=15

#window size
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

#center x,y and radius
STARTX0=WIDTH//2
STARTY0=HEIGHT//2
RADIUS0=random.randint(STARTY0//8,STARTY0//4)
RADIUS1=random.randint(STARTY0//8,STARTY0//4)
RADIUS2=random.randint(STARTY0//8,STARTY0//4)
RADIUS3=random.randint(STARTY0//8,STARTY0//4)
print(RADIUS0, RADIUS1, RADIUS2, RADIUS3)

# gravity
G=9.81

#Start angle and velocity
#0=up, 90=right, 180=down, 270=left
#Try different angles to see what happens
STARTANGLE0=random.randint(0,359)
STARTANGLE1=random.randint(0,359)
STARTANGLE2=random.randint(0,359)
STARTANGLE3=random.randint(0,359)
print(STARTANGLE0, STARTANGLE1, STARTANGLE2, STARTANGLE3)

#>0 =>counter-clockwise
#<0 =>clockwise
#otherwise side to side
#higher initial velocity=>higher speed
STARTVELOCITY0=random.uniform(-0.05, 0.05)
STARTVELOCITY1=random.uniform(-0.05, 0.05)
STARTVELOCITY2=random.uniform(-0.05, 0.05)
STARTVELOCITY3=random.uniform(-0.05, 0.05)
print(STARTVELOCITY0, STARTVELOCITY1, STARTVELOCITY2, STARTVELOCITY3)

INFLUENCE0=0#random.uniform(0, 0.05)
INFLUENCE1=0#random.uniform(0, 0.05)
INFLUENCE2=0#random.uniform(0, 0.05)
print(INFLUENCE0, INFLUENCE1, INFLUENCE2)

#delta time
DT=0.05

##############################################################################
#variables
##############################################################################
# Physical properties and initial conditions for pendulum
# initial upper angle (from vertical)
theta0=radians(STARTANGLE0)
theta1=radians(STARTANGLE1)
theta2=radians(STARTANGLE2)
theta3=radians(STARTANGLE3)

# start pendulum at start
velocity0=STARTVELOCITY0
velocity1=STARTVELOCITY1
velocity2=STARTVELOCITY2
velocity3=STARTVELOCITY3




##############################################################################
#functions
##############################################################################

##############################################################################
#initial code
##############################################################################
#initialize the pygame environment


# you have to call this at the start if you want to use this module.
pygame.font.init()

# creates a clock
clock=pygame.time.Clock()

#choose font for later use
myfont = pygame.font.SysFont('Courier', 12)

# set up the window with size and caption
screen = pygame.display.set_mode((WIDTH, HEIGHT))#, pygame.FULLSCREEN)
ball = pygame.surface.Surface((WIDTH, HEIGHT))
ball.fill(twhcolors.SILVER)
pygame.display.set_caption('Pendelum')
#pygame.mouse.set_visible(False)

##############################################################################
#main loop
##############################################################################
while True:
    #limit updates to FPS
    clock.tick(FPS)

    #draw background color to blank the screen
    screen.fill(twhcolors.YELLOW)

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

    # Calculate accelleration due to gravity
    accel0=-(G/RADIUS0)*sin(theta0)
    # Change velocity according to accelleration
    velocity0+=accel0*DT
    # Change angle according to (updated) velocity
    theta0-=velocity0

    # Calculate accelleration due to gravity
    accel1=-(G/RADIUS1)*sin(theta1)-accel0*INFLUENCE0
    # Change velocity according to accelleration
    velocity1+=accel1*DT
    # Change angle according to (updated) velocity
    theta1-=velocity1

    # Calculate accelleration due to gravity
    accel2=-(G/RADIUS2)*sin(theta2)-accel1*INFLUENCE1
    # Change velocity according to accelleration
    velocity2+=accel2*DT
    # Change angle according to (updated) velocity
    theta2-=velocity2

    # Calculate accelleration due to gravity
    accel3=-(G/RADIUS3)*sin(theta3)-accel2*INFLUENCE2
    # Change velocity according to accelleration
    velocity3+=accel3*DT
    # Change angle according to (updated) velocity
    theta3-=velocity3

    #calculate new position for the ball
    stopx0=STARTX0+int(RADIUS0*sin(theta0))
    stopy0=STARTY0-int(RADIUS0*cos(theta0))

    stopx1=stopx0+int(RADIUS1*sin(theta1))
    stopy1=stopy0-int(RADIUS1*cos(theta1))

    stopx2=stopx1+int(RADIUS2*sin(theta2))
    stopy2=stopy1-int(RADIUS2*cos(theta2))

    stopx3=stopx2+int(RADIUS3*sin(theta3))
    stopy3=stopy2-int(RADIUS3*cos(theta3))

    #draw new pendulum
    pygame.gfxdraw.box(ball, pygame.Rect(0,0,WIDTH,HEIGHT), (255,255,255,3))
    pygame.draw.circle(ball, twhcolors.GREEN, (stopx3, stopy3), 5, 0)
    screen.blit(ball, [0,0])

    pygame.draw.line(screen, twhcolors.BLUE, (STARTX0, STARTY0), (stopx0, stopy0))
    pygame.draw.line(screen, twhcolors.BLUE, (stopx0, stopy0), (stopx1, stopy1))
    pygame.draw.circle(screen, twhcolors.RED, (stopx0, stopy0), 5, 0)
    pygame.draw.line(screen, twhcolors.BLUE, (stopx1, stopy1), (stopx2, stopy2))
    pygame.draw.circle(screen, twhcolors.RED, (stopx1, stopy1), 5, 0)
    pygame.draw.line(screen, twhcolors.BLUE, (stopx2, stopy2), (stopx3, stopy3))
    pygame.draw.circle(screen, twhcolors.RED, (stopx2, stopy2), 5, 0)
    pygame.draw.circle(screen, twhcolors.WHITE, (STARTX0, STARTY0), 5, 0)

    #update display
    pygame.display.flip()
