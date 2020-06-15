#Description
#Generating and drawing L-systems
#For description of lsystems: https://en.wikipedia.org/wiki/L-system
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com
import lsystem

"""
Drawing with Lindenmayer system
F: Draw
+: Turn right
-: Turn left
90 degree angle on turns
X: Control variable

name: The name of the creation (string)
axiom: start condition (string)
rules: build rules (dictionary)
generations: how many generations to compute(int)
length: length of each line(int)
angle: angle of turns(int)
heading: initial heading(int)
offsetx, offsety: move the startpoint for drawing(int) 0,0 is defined as WIDTH/2,HEIGHT/2
"""

name="Example 6: Dragon curve"
axiom="FX"
rules={"X":"X+YF+", "Y":"-FX-Y"}
generations=10
angle=90
heading=180
offsetx=0
offsety=0
length=5

ls=lsystem.Lsystem(name, axiom, rules, generations, length, angle, heading, offsetx, offsety)
ls.generate()
ls.draw()
