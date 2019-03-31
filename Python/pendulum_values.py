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

# gravity
G=9.81

#window size
WIDTH, HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h

#center x,y and radius
STARTX0=WIDTH//2
STARTY0=HEIGHT//2
RADIUS0=random.randint(STARTY0//8,STARTY0//5)
RADIUS1=random.randint(STARTY0//8,STARTY0//5)
RADIUS2=random.randint(STARTY0//8,STARTY0//5)
RADIUS3=random.randint(STARTY0//8,STARTY0//5)
RADIUS4=random.randint(STARTY0//8,STARTY0//5)
print(RADIUS0, RADIUS1, RADIUS2, RADIUS3, RADIUS4)

#Start angle and velocity
#0=up, 90=right, 180=down, 270=left
STARTANGLE0=random.randint(0,359)
STARTANGLE1=random.randint(0,359)
STARTANGLE2=random.randint(0,359)
STARTANGLE3=random.randint(0,359)
STARTANGLE4=random.randint(0,359)
print(STARTANGLE0, STARTANGLE1, STARTANGLE2, STARTANGLE3, STARTANGLE4)

#>0 =>counter-clockwise
#<0 =>clockwise
STARTVELOCITY0=random.uniform(-0.1, 0.1)
STARTVELOCITY1=random.uniform(-0.1, 0.1)
STARTVELOCITY2=random.uniform(-0.1, 0.1)
STARTVELOCITY3=random.uniform(-0.1, 0.1)
STARTVELOCITY4=random.uniform(-0.1, 0.1)
print(STARTVELOCITY0, STARTVELOCITY1, STARTVELOCITY2, STARTVELOCITY3, STARTVELOCITY4)

INFLUENCE00=random.uniform(-0.1, 0.1)
INFLUENCE01=random.uniform(-0.1, 0.1)
INFLUENCE02=random.uniform(-0.1, 0.1)
INFLUENCE03=random.uniform(-0.1, 0.1)
INFLUENCE04=random.uniform(-0.1, 0.1)
INFLUENCE10=random.uniform(-0.1, 0.1)
INFLUENCE11=random.uniform(-0.1, 0.1)
INFLUENCE12=random.uniform(-0.1, 0.1)
INFLUENCE13=random.uniform(-0.1, 0.1)
INFLUENCE14=random.uniform(-0.1, 0.1)
print(INFLUENCE00, INFLUENCE01, INFLUENCE02, INFLUENCE03, INFLUENCE04)
print(INFLUENCE10, INFLUENCE11, INFLUENCE12, INFLUENCE13, INFLUENCE14)

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
theta4=radians(STARTANGLE4)

# start pendulum at start
velocity0=STARTVELOCITY0
velocity1=STARTVELOCITY1
velocity2=STARTVELOCITY2
velocity3=STARTVELOCITY3
velocity4=STARTVELOCITY4

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
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
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
    accel1=-(G/RADIUS1)*sin(theta1)-accel0*INFLUENCE00
    accel2=-(G/RADIUS2)*sin(theta2)-accel1*INFLUENCE01
    accel3=-(G/RADIUS3)*sin(theta3)-accel2*INFLUENCE02
    accel4=-(G/RADIUS3)*sin(theta4)-accel3*INFLUENCE03
    accel3-=accel4*INFLUENCE14
    accel2-=accel3*INFLUENCE13
    accel1-=accel2*INFLUENCE12
    accel0-=accel1*INFLUENCE11

    # Change velocity according to accelleration
    velocity0+=accel0*DT
    # Change angle according to (updated) velocity
    theta0-=velocity0

    # Change velocity according to accelleration
    velocity1+=accel1*DT
    # Change angle according to (updated) velocity
    theta1-=velocity1

    # Change velocity according to accelleration
    velocity2+=accel2*DT
    # Change angle according to (updated) velocity
    theta2-=velocity2

    # Change velocity according to accelleration
    velocity3+=accel3*DT
    # Change angle according to (updated) velocity
    theta3-=velocity3

    # Change velocity according to accelleration
    velocity4+=accel4*DT
    # Change angle according to (updated) velocity
    theta4-=velocity4

    #calculate new position for the ball
    stopx0=STARTX0+int(RADIUS0*sin(theta0))
    stopy0=STARTY0-int(RADIUS0*cos(theta0))

    stopx1=stopx0+int(RADIUS1*sin(theta1))
    stopy1=stopy0-int(RADIUS1*cos(theta1))

    stopx2=stopx1+int(RADIUS2*sin(theta2))
    stopy2=stopy1-int(RADIUS2*cos(theta2))

    stopx3=stopx2+int(RADIUS3*sin(theta3))
    stopy3=stopy2-int(RADIUS3*cos(theta3))

    stopx4=stopx3+int(RADIUS4*sin(theta4))
    stopy4=stopy3-int(RADIUS4*cos(theta4))

    #draw new pendulum
    pygame.gfxdraw.box(ball, pygame.Rect(0,0,WIDTH,HEIGHT), (255,255,255,3))
    pygame.draw.circle(ball, twhcolors.GREEN, (stopx4, stopy4), 5, 0)
    screen.blit(ball, [0,0])

    pygame.draw.line(screen, twhcolors.BLUE, (STARTX0, STARTY0), (stopx0, stopy0))
    pygame.draw.line(screen, twhcolors.BLUE, (stopx0, stopy0), (stopx1, stopy1))
    pygame.draw.circle(screen, twhcolors.RED, (stopx0, stopy0), 5, 0)
    pygame.draw.line(screen, twhcolors.BLUE, (stopx1, stopy1), (stopx2, stopy2))
    pygame.draw.circle(screen, twhcolors.RED, (stopx1, stopy1), 5, 0)
    pygame.draw.line(screen, twhcolors.BLUE, (stopx2, stopy2), (stopx3, stopy3))
    pygame.draw.circle(screen, twhcolors.RED, (stopx2, stopy2), 5, 0)
    pygame.draw.line(screen, twhcolors.BLUE, (stopx3, stopy3), (stopx4, stopy4))
    pygame.draw.circle(screen, twhcolors.RED, (stopx3, stopy3), 5, 0)
    pygame.draw.circle(screen, twhcolors.WHITE, (STARTX0, STARTY0), 5, 0)

    #update display
    pygame.display.flip()
