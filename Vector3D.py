#IMPORT STATEMENTS
#Needed for the trig functions to do calculations for the 
#magnitude and angle given the x and y components
import math 
from Vector import *
####################################################################################################

#EXTENDS VECTOR CLASS
class Vector3D(Vector):

#PROPERTIES FOR CLASS
    
    #Needed because 3D vector has an extra component
    z_component = 0
   
    #These are for defining angle direction for 3D vector
    angle_x = 0
    angle_y = 0
    angle_z = 0

####################################################################################################
# CONSTRUCTOR 

    def __init__(self, x_comp, y_comp, z_comp):
        self.x_component = x_comp
        self.y_component = y_comp
        self.z_component = z_comp

####################################################################################################
# GETTERS

    def get_z_component(self):
        return self.z_component
    
####################################################################################################
# SETTERS 

   
    def set_z_component(self, y_comp):
        self.y_component = z_comp

####################################################################################################
# METHODS

    # These methods get the magnitude and angle properties from the x, y, and z component properties.
    def calcMagnitude(self):
        self.magnitude = math.sqrt((self.x_component**2) + (self.y_component**2) + (self.z_component**2))

    #TODO IMPLEMENT CORRECT ANGLE CALCULATION FOR 3D VECTOR
    def calcAngle(self):
         self.angle = math.acos(self.x_component/self.magnitude) 

    #Added method to print z component to console
    def printZComponent(self) :
        print("The z component is " + str(self.z_component))"\ty component = " + str(self.z_component)

    #Method to print string containing components for 3D vector to console.
    def printComponents(self) :
        print("x component = " + str(self.x_component) + "\ty component = " + str(self.y_component) + "\ty component = " + str(self.z_component))

    #Overrides parent printAngle method because 3D vectors have 3 values defining angle
    #TODO make sure to implement Print statement for 3 angles of 3D vector.
    def printAngle(self) :
        print("The angle is " + str(self.angle) + " radians")
