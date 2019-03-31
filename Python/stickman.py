import pygame, sys
from pygame.locals import *

WIDTH=400
HEIGHT=400

class BodyPart:
    def __init__(self, screen, color, left, top, radius, theta, mintheta, maxtheta, name):
        self.screen=screen
        self.color=color
        self.left=left
        self.top=top
        self.radius=radius
        self.theta=theta
        self.mintheta=mintheta
        self.maxtheta=maxtheta
        self.name=name

    def paint(self):
        #conversion from polar to cartesian
        stopx=self.left+int(self.radius*sin(self.theta))
        stopy=self.top-int(RADIUS0*cos(self.theta))
        #paint line
        pygame.draw.line(screen, self.color, (self.left, self.top), (stopx, stopy))

    def __repr__(self):
        return "<"+self.name+" "+str(self.left)+" "+str(self.top)+" "+str(self.radius)+">"

##############################################################################
#variables
##############################################################################
screen=1
bodyparts=[]

bp=BodyPart(screen, (0,0,0), 0, 0, 100, 180, -180, 180, "torso")
bodyparts.append([bp, 0, -1])

bp=BodyPart(screen, (0,0,0), 0, 0, 5, 270, -10, 10, "humero_sinister")
bodyparts.append([bp, 1, -1])

bp=BodyPart(screen, (0,0,0), 0, 0, 5, 90, -10, 10, "humero_dexter")
bodyparts.append([bp, 2, -1])

bp=BodyPart(screen, (0,0,0), 0, 0, 10, 0, -10, 10, "collum")
bodyparts.append([bp, 3, -1])

bp=BodyPart(screen, (0,0,0), 0, 0, 30, 0, -10, 10, "caput")
bodyparts.append([bp, 4, 3])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 190, -180, 180, "brachium_sinister")
bodyparts.append([bp, 5, 1])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 190, -180, 180, "antebrachium_sinister")
bodyparts.append([bp, 6, 5])

bp=BodyPart(screen, (0,0,0), 0, 0, 10, 190, -180, 180, "manibus_sinister")
bodyparts.append([bp, 7, 6])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 170, -180, 180, "brachium_dexter")
bodyparts.append([bp, 8, 2])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 170, -180, 180, "antebrachium_dexter")
bodyparts.append([bp, 9, 8])

bp=BodyPart(screen, (0,0,0), 0, 0, 10, 170, -180, 180, "manibus_dexter")
bodyparts.append([bp,10, 9])

bp=BodyPart(screen, (0,0,0), 0, 0, 5, 270, -10, 10, "pelvis_sinister")
bodyparts.append([bp,11, 0])

bp=BodyPart(screen, (0,0,0), 0, 0, 5, 90, -10, 10, "pelvis_dexter")
bodyparts.append([bp,12, 0])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 190, -10, 10, "femur_sinister")
bodyparts.append([bp,12,11])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 190, -10, 10, "tibia_sinister")
bodyparts.append([bp,13,12])

bp=BodyPart(screen, (0,0,0), 0, 0, 10, 190, -10, 10, "pes_sinister")
bodyparts.append([bp,14,13])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 170, -10, 10, "femur_dexter")
bodyparts.append([bp,15,12])

bp=BodyPart(screen, (0,0,0), 0, 0, 50, 170, -10, 10, "tibia_dexter")
bodyparts.append([bp,16,15])

bp=BodyPart(screen, (0,0,0), 0, 0, 10, 170, -10, 10, "pes_dexter")
bodyparts.append([bp,17,16])

for x in bodyparts:
    print(x)
