#Basic vector parent class defining base properties we would expect any vector to have
#All vectors will share some commonalities and this parent class captures that.

#IMPORT STATEMENTS
####################################################################################################
class Vector:

#PROPERTIES FOR CLASS

    x_component = 0
    y_component = 0
    magnitude   = 0
    angle       = 0

####################################################################################################
# CONSTRUCTOR 

    def __init__(self, x_comp, y_comp):
        self.x_component = x_comp
        self.y_component = y_comp

####################################################################################################
# GETTERS

    def get_x_component(self):
        return self.x_component
   
    def get_y_component(self):
        return self.y_component

    def get_magnitude(self):
        return self.magnitude
    
    def get_angle(self):
        return self.angle
####################################################################################################
# SETTERS 

    def set_x_component(self, x_comp):
        self.x_component = x_comp
   
    def set_y_component(self, y_comp):
        self.y_component = y_comp

    def set_magnitude(self, magn):
        self.magnitude = magn
    
    def set_angle(self, ang):
        self.angle = ang

####################################################################################################
# METHODS


# Methods to print object properties

    def printMagnitude(self):
        print("The magnitude is " + str(self.magnitude))
    
    def printXComponent(self):
        print("The x component is " + str(self.x_component))
   
    def printYComponent(self) :
        print("The y component is " + str(self.y_component))
 
    def printAngle(self) :
        print("The angle is " + str(self.angle) + " radians")
