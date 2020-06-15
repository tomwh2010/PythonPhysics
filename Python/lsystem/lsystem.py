#Description
#Generating and drawing L-systems
#For description of lsystems: https://en.wikipedia.org/wiki/L-system
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import pygame, sys
from pygame.locals import *
import math

class Lsystem:
    """
    name: The name of the creation (string)
    axiom: start condition (string)
    rules: build rules (dictionary)
    generations: how many generations to compute(int)
    length: length of each line(int)
    angle: angle of turns(int)
    heading: initial heading(int)
    offsetx, offsety: move the startpoint for drawing(int) 0,0 is defined as WIDTH/2,HEIGHT/2
    """
    def __init__(self, name, axiom, rules, generations, length, angle, heading, offsetx, offsety):
        #how many frames pr second
        self.fps=25
        #width of the window
        self.width=800
        #height of the window
        self.height=600
        #thickness of the line
        self.linethickness=1
        #name of the creation
        self.name=name

        #backgroundcolor
        self.linecolor=pygame.Color("black")
        #linecolor
        self.bgcolor=pygame.Color("white")
        
        #init the pygame system
        pygame.init()

        # set up the window with size and caption
        self.screen=pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Lsystem')

        # creates internal game clock
        self.clock=pygame.time.Clock()

        #sets variables from __init__
        self.offsetx=offsetx
        self.offsety=offsety
        self.rules=rules
        self.angle=angle
        self.generations=generations
        self.length=length
        self.axiom=axiom

        #center xy
        self.centerx=self.width/2
        self.centery=self.height/2

        #set initial settings
        self.x=self.centerx+self.offsetx
        self.y=self.centery+self.offsety
        self.heading=heading
        self.running=True
        self.states=[]
        self.sentence=self.axiom

    #turn left, clamped to 0-359
    def left(self):
        self.heading=(-self.angle+self.heading+360)%360
    
    #turn right, clamped to 0-359
    def right(self):
        self.heading=(self.angle+self.heading+360)%360

    #push current state
    def pushState(self):
        currentstate=[self.x, self.y, self.heading, self.length]
        self.states.append(currentstate)

    #pop current state, populate variables
    def popState(self):
        currentstate=self.states.pop()
        self.x=currentstate[0]
        self.y=currentstate[1]
        self.heading=currentstate[2]
        self.length=currentstate[3]
    
    #move forward and possibly draw
    def forward(self, draw=True):
        #calculate x1,y1 using polar->cartesian coordinates
        #https://en.wikipedia.org/wiki/List_of_common_coordinate_transformations
        theta=math.radians(self.heading)
        x1=self.x+int(self.length*math.sin(theta))
        y1=self.y+int(self.length*math.cos(theta))
        #draw if we have to
        if draw:
            pygame.draw.line(self.screen, self.linecolor, (self.x, self.y), (x1, y1), self.linethickness)

        #set new position
        self.x=x1
        self.y=y1
    
    #wrapper for move only
    def move(self):
        self.forward(draw=False)

    #generate string according to rules
    #stop at required max generations
    def generate(self):
        for i in range(self.generations):
            newsentence=""
            for o in self.sentence:
                char=o
                if o in self.rules:            
                    char=self.rules[o]
                newsentence+=char
            self.sentence=newsentence

    #drawing function
    def draw(self):
        running=True

        #draw background color to blank the screen
        self.screen.fill(self.bgcolor)

        # you have to call this at the start if you want to use this module.
        pygame.font.init()

        #choose font for later use
        myfont = pygame.font.SysFont('Courier', 24)

        #render buffer as picture
        textsurface=myfont.render(self.name, 1, pygame.Color("black"))
        
        #main loop
        while True:
            #limit updates to FPS
            self.clock.tick(self.fps)

            #get events from the event queue
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit

            #draw the generated string
            if running:
                print("System length",len(self.sentence))

                #for each char in sentence
                #do the necessary function
                for c in self.sentence:
                    if c=="F" or c=="G" or c=="A" or c=="B":
                        self.forward()
                    if c=="f" or c=="g" or c=="a" or c=="b":
                        self.move()
                    if c=="-":
                        self.left()
                    if c=="+":
                        self.right()
                    if c=="[":
                        self.pushState()
                    if c=="]":
                        self.popState()

                #paint picture to screen at location 130,180
                self.screen.blit(textsurface,(10, 10))

            running=False

            pygame.display.flip()

if __name__=="__main__":        
    """
    Drawing with Lindenmayer system
    F: Draw
    +: Turn right
    -: Turn left
    90 degree angle on turns
    X: Control variable
    """
    name="Example 7: Fractal plant"
    axiom="X"
    rules={"X":"F+[[X]-X]-F[-FX]+X", "F":"FF"}
    generations=6
    angle=25
    heading=180-angle
    offsetx=-100
    offsety=300
    length=4
    
    ls=Lsystem(name, axiom, rules, generations, length, angle, heading, offsetx, offsety)
    ls.generate()
    ls.draw()
    