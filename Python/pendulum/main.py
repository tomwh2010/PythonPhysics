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
from pendulum import RandomPendulum

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

#delta time
DT=0.05

pd=RandomPendulum()

##############################################################################
#variables
##############################################################################
# Physical properties and initial conditions for pendulum
# initial upper angle (from vertical)
theta0=radians(pd.startangle0)
theta1=radians(pd.startangle1)
theta2=radians(pd.startangle2)
theta3=radians(pd.startangle3)
theta4=radians(pd.startangle4)

# start pendulum at start
velocity0=pd.startvelocity0
velocity1=pd.startvelocity1
velocity2=pd.startvelocity2
velocity3=pd.startvelocity3
velocity4=pd.startvelocity4

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
    accel0=-(G/pd.radius0)*sin(theta0)
    accel1=-(G/pd.radius1)*sin(theta1)-accel0*pd.influence00
    accel2=-(G/pd.radius2)*sin(theta2)-accel1*pd.influence01
    accel3=-(G/pd.radius3)*sin(theta3)-accel2*pd.influence02
    accel4=-(G/pd.radius3)*sin(theta4)-accel3*pd.influence03
    accel3-=accel4*pd.influence14
    accel2-=accel3*pd.influence13
    accel1-=accel2*pd.influence12
    accel0-=accel1*pd.influence11

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
    stopx0=STARTX0+int(pd.radius0*sin(theta0))
    stopy0=STARTY0-int(pd.radius0*cos(theta0))

    stopx1=stopx0+int(pd.radius1*sin(theta1))
    stopy1=stopy0-int(pd.radius1*cos(theta1))

    stopx2=stopx1+int(pd.radius2*sin(theta2))
    stopy2=stopy1-int(pd.radius2*cos(theta2))

    stopx3=stopx2+int(pd.radius3*sin(theta3))
    stopy3=stopy2-int(pd.radius3*cos(theta3))

    stopx4=stopx3+int(pd.radius4*sin(theta4))
    stopy4=stopy3-int(pd.radius4*cos(theta4))

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
