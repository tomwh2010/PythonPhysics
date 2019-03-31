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

class Pendulum:
    def __init__(self):
        pygame.init()

        self.radius0=50
        self.radius1=50
        self.radius2=50
        self.radius3=50
        self.radius4=50

        self.angle0=0
        self.angle1=0
        self.angle2=0
        self.angle3=0
        self.angle4=0

        self.velocity0=0
        self.velocity1=0
        self.velocity2=0
        self.velocity3=0
        self.velocity4=0

        self.cycle=0

        self.influence00=0
        self.influence01=0
        self.influence02=0
        self.influence03=0
        self.influence04=0
        self.influence10=0
        self.influence11=0
        self.influence12=0
        self.influence13=0
        self.influence14=0

        #window size
        self.width, self.height = 600,600#pygame.display.Info().current_w, pygame.display.Info().current_h

        self.radiustotal=self.height//2
        if self.width<self.height:
            self.radiustotal=width//2

        self.fps=15

        # gravity
        self.G=9.81

        #center x,y and radius
        self.startx0=self.width//2
        self.starty0=self.height//2

        #delta time
        self.dt=0.05

        # Physical properties and initial conditions for pendulum
        # initial upper angle (from vertical)
        self.theta0=radians(self.angle0)
        self.theta1=radians(self.angle1)
        self.theta2=radians(self.angle2)
        self.theta3=radians(self.angle3)
        self.theta4=radians(self.angle4)

    def printvalues():
        print(self.radius0, self.radius1, self.radius2, self.radius3, self.radius4)
        print(self.velocity0, self.velocity1, self.velocity2, self.velocity3, self.velocity4)
        print(self.angle0, self.angle1, self.angle2, self.angle3, self.angle4)
        print(self.influence00, self.influence01, self.influence02, self.influence03, self.self.influence04)
        print(self.influence10, self.self.influence11, self.self.influence12, self.self.influence13, self.self.influence14)

    def start(self):
        # you have to call this at the start if you want to use this module.
        pygame.font.init()

        # creates a clock
        self.clock=pygame.time.Clock()

        # set up the window with size and caption
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
        self.ball = pygame.surface.Surface((self.width, self.height))
        self.ball.fill(twhcolors.SILVER)
        pygame.display.set_caption('Pendelum')
        #pygame.mouse.set_visible(False)

##############################################################################
#main loop
##############################################################################
    def draw(self):
        while True:
            #limit updates to FPS
            self.clock.tick(self.fps)

            #draw background color to blank the screen
            self.screen.fill(twhcolors.YELLOW)

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
            self.accel0=-(self.G/self.radius0)*sin(self.theta0)
            self.accel1=-(self.G/self.radius1)*sin(self.theta1)
            self.accel2=-(self.G/self.radius2)*sin(self.theta2)
            self.accel3=-(self.G/self.radius3)*sin(self.theta3)
            self.accel4=-(self.G/self.radius4)*sin(self.theta4)

            for i in range(self.cycle):
                self.accel1-=self.accel0*self.influence00
                self.accel2-=self.accel1*self.influence01
                self.accel3-=self.accel2*self.influence02
                self.accel4-=self.accel3*self.influence03

                self.accel3-=self.accel4*self.influence14
                self.accel2-=self.accel3*self.influence13
                self.accel1-=self.accel2*self.influence12
                self.accel0-=self.accel1*self.influence11

            # Change velocity according to accelleration
            self.velocity0+=self.accel0*self.dt
            # Change angle according to (updated) velocity
            self.theta0-=self.velocity0

            # Change velocity according to accelleration
            self.velocity1+=self.accel1*self.dt
            # Change angle according to (updated) velocity
            self.theta1-=self.velocity1

            # Change velocity according to accelleration
            self.velocity2+=self.accel2*self.dt
            # Change angle according to (updated) velocity
            self.theta2-=self.velocity2

            # Change velocity according to accelleration
            self.velocity3+=self.accel3*self.dt
            # Change angle according to (updated) velocity
            self.theta3-=self.velocity3

            # Change velocity according to accelleration
            self.velocity4+=self.accel4*self.dt
            # Change angle according to (updated) velocity
            self.theta4-=self.velocity4

            #calculate new position for the ball
            self.stopx0=self.startx0+int(self.radius0*sin(self.theta0))
            self.stopy0=self.starty0-int(self.radius0*cos(self.theta0))

            self.stopx1=self.stopx0+int(self.radius1*sin(self.theta1))
            self.stopy1=self.stopy0-int(self.radius1*cos(self.theta1))

            self.stopx2=self.stopx1+int(self.radius2*sin(self.theta2))
            self.stopy2=self.stopy1-int(self.radius2*cos(self.theta2))

            self.stopx3=self.stopx2+int(self.radius3*sin(self.theta3))
            self.stopy3=self.stopy2-int(self.radius3*cos(self.theta3))

            self.stopx4=self.stopx3+int(self.radius4*sin(self.theta4))
            self.stopy4=self.stopy3-int(self.radius4*cos(self.theta4))

            #draw new pendulum
            pygame.gfxdraw.box(self.ball, pygame.Rect(0,0,self.width,self.height), (255,255,255,3))
            pygame.draw.circle(self.ball, twhcolors.GREEN, (self.stopx4, self.stopy4), 5, 0)
            self.screen.blit(self.ball, [0,0])

            pygame.draw.line(self.screen, twhcolors.BLUE, (self.startx0, self.starty0), (self.stopx0, self.stopy0))
            pygame.draw.line(self.screen, twhcolors.BLUE, (self.stopx0, self.stopy0), (self.stopx1, self.stopy1))
            pygame.draw.circle(self.screen, twhcolors.RED, (self.stopx0, self.stopy0), 5, 0)
            pygame.draw.line(self.screen, twhcolors.BLUE, (self.stopx1, self.stopy1), (self.stopx2, self.stopy2))
            pygame.draw.circle(self.screen, twhcolors.RED, (self.stopx1, self.stopy1), 5, 0)
            pygame.draw.line(self.screen, twhcolors.BLUE, (self.stopx2, self.stopy2), (self.stopx3, self.stopy3))
            pygame.draw.circle(self.screen, twhcolors.RED, (self.stopx2, self.stopy2), 5, 0)
            pygame.draw.line(self.screen, twhcolors.BLUE, (self.stopx3, self.stopy3), (self.stopx4, self.stopy4))
            pygame.draw.circle(self.screen, twhcolors.RED, (self.stopx3, self.stopy3), 5, 0)
            pygame.draw.circle(self.screen, twhcolors.WHITE, (self.startx0, self.starty0), 5, 0)

            #update display
            pygame.display.flip()

class RandomPendulum(Pendulum):
    def __init__(self):
        super().__init__()
        self.radius0=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius1=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius2=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius3=random.randint(self.radiustotal//8,self.radiustotal//5)
        self.radius4=random.randint(self.radiustotal//8,self.radiustotal//5)

        self.angle0=random.randint(0,359)
        self.angle1=random.randint(0,359)
        self.angle2=random.randint(0,359)
        self.angle3=random.randint(0,359)
        self.angle4=random.randint(0,359)

        self.velocity0=random.uniform(-0.1, 0.1)
        self.velocity1=random.uniform(-0.1, 0.1)
        self.velocity2=random.uniform(-0.1, 0.1)
        self.velocity3=random.uniform(-0.1, 0.1)
        self.velocity4=random.uniform(-0.1, 0.1)

        self.influence00=random.uniform(-0.1, 0.1)
        self.influence01=random.uniform(-0.1, 0.1)
        self.influence02=random.uniform(-0.1, 0.1)
        self.influence03=random.uniform(-0.1, 0.1)
        self.influence04=random.uniform(-0.1, 0.1)
        self.influence10=random.uniform(-0.1, 0.1)
        self.influence11=random.uniform(-0.1, 0.1)
        self.influence12=random.uniform(-0.1, 0.1)
        self.influence13=random.uniform(-0.1, 0.1)
        self.influence14=random.uniform(-0.1, 0.1)

        self.cycle=3


class SimplePendulum(Pendulum):
    def __init__(self):
        super().__init__()
        self.velocity0=.01
        self.velocity1=.01
        self.velocity2=.01
        self.velocity3=.01
        self.velocity4=.01


class SpiralPendulum(Pendulum):
    def __init__(self):
        super().__init__()
        self.velocity0=0.01
        self.velocity1=0.02
        self.velocity2=0.03
        self.velocity3=0.04
        self.velocity4=0.05
        self.G=0

if __name__=="__main__":
    pd=SpiralPendulum()
    pd.start()
    pd.draw()
