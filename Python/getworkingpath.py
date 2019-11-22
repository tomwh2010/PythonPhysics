#Description
#Auxiliary file
#Give the correct path to the working directory
#Anaconda probably does not need it, Visual Code does
#
#usage:
#from getworkingpath import *
#filename=getworkingpath()+"/fakenews1.wav"
#
#Part of the pygame series at https://github.com/tomwh2010/PythonPhysics
#Public domain by tomwh2010@hotmail.com

import sys, os

def getworkingpath():          
    pathname = os.path.dirname(sys.argv[0])    
    return os.path.abspath(pathname)