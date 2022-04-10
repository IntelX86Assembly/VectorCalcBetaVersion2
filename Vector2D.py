#IMPORT STATEMENTS
#Needed for the trig functions to do calculations for the 
#magnitude and angle given the x and y components
import math 
from Vector import *
####################################################################################################

#EXTENDS VECTOR CLASS
class Vector2D(Vector):

# METHODS

    #These methods calculate the magnitude and angle properties from the x and y 
    #component properties. These extend the vector class because different 
    #vectors do these operations differently. For instance a 3D vector would
    #compute its magnitude and angle in a different way
    def calcMagnitude(self):
        self.magnitude = math.sqrt((self.x_component**2) + (self.y_component**2))

    def calcAngle(self):
         self.angle = math.acos(self.x_component/self.magnitude) 
 
    def toString(self): 
        print("X = " + str(self.get_x_component()) + "   Y = " + str(self.get_y_component()))  
