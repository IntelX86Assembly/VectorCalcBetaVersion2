from Vector2D import *

class VectorList2D():


    
# CONSTRUCTOR     
    def __init__(self):
        #holds a list of Vector2D objects.
        self.listVectors = []
        self.outputString = ""
        #If vector components need to be summed these variables will hold the result
        self.sumComponentsX = 0 
        self.sumComponentsY = 0 
        self.counter = 0

################################################################################
# GETTERS

    def getSumX(self):
        return self.sumComponentsX

    def getSumY(self):
        return self.sumComponentsY

    def getOutputString(self):
        return self.outputString
    
    def getSize(self):
        return len(self.listVectors)
    
    def getVectorList(self):
        return self.listVectors
################################################################################
# SETTERS
    
    def setOutputString(self, outputString):
        self.outputString = outputString

    def setSumX(self, sumComponentsX):
        self.sumComponentsX = sumComponentsX

    def setSumY(self, sumComponentsY):
        self.sumComponentsY = sumComponentsY

    def clearListVectors(self, listVectors):
        self.listVectors.clear()

################################################################################
# Helper Function Methods

    #Appends a vector to the list
    def addVector2D(self, componentX, componentY):
        self.listVectors.append(Vector2D(float(componentX), float(componentY)))

    #Sums vectors in the list convienient for some calculations 
    def sumVectors(self):
       for vector in self.listVectors:
            self.sumComponentsX += vector.get_x_component()
            self.sumComponentsY += vector.get_y_component()
    
    def findEquilibriumVector(self):
       for vector in self.listVectors:
            self.sumComponentsX = -self.sumComponentsX
            self.sumComponentsY = -self.sumComponentsY


        #Pops items in list like a stack so that user can undo actions
    def removeVector(self):
        self.listVectors.pop()

    #appends to stringArray whenever the user adds a vector to the list.
    def toString(self):
        self.outputString = ""
        self.counter = 0
        #For every vector in the list we are adding them to do the following
        for vector2D in self.listVectors:
            self.counter = self.counter + 1
            #Create a string that displays user entered values
            self.outputString += ("\n" + "Vector " + str(self.counter) +  ":   X = " + str(vector2D.get_x_component()) + "   Y = " + str(vector2D.get_y_component()))
        return self.outputString


