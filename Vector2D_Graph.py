#IMPORT STATEMENTS
import math 

#import pyplot to plot the vectors in a graph
import matplotlib.pyplot as plotter

#import the vector classes to instantiate vector objects
#and gain access to their properties and methods
from Vector2D import *

####################################################################################################
class Vector2D_Graph:

#PROPERTIES FOR CLASS
    origin_points = []
    x_components = []
    y_components = []
    scaleSize = 0


####################################################################################################
    # CONSTRUCTOR 
    #TODO IMPLEMENT CONSTRUCTOR
    def __init__(self):
        pass
####################################################################################################
    # GETTERS

    def get_x_components(self):
        return self.x_components

    def get_y_components(self):
        return self.y_components

    def get_origin_points(self):
        return self.origin_points

    def get_scaleSize(self):
        return self.scaleSize

####################################################################################################
# SETTERS 

    def set_x_components(self, x_comp):
        self.x_components = x_comp
   
    def set_y_components(self, y_comp):
        self.y_components = y_comp

    def set_origin_points(self, origin):
        self.origin_points = origin
    
    def set_scaleSize(self, scale):
        self.scaleSize = scale

####################################################################################################
# METHODS

    #Calculates the scale size for the window drawn for the graph. Doen to scale
    #The window automatically. It takes a vector list and compares the vector magnitudes 
    #of the vectors in the vector list and scales the graph by comparing these values
    def calcScaleNonresultant(self, vectorList):
        prevMax = 0 
        scaleSize = 0
        for vector in vectorList.getVectorList():
            # Gets the max value of the current vector either x component or 
            # y component and checks if it is bigger than the largest vector
            # component. This is done to scale the window automatically.

            biggestComp= max(abs(vector.get_x_component()), abs(vector.get_y_component()))
            if biggestComp > prevMax:
               prevMax = biggestComp
               scaleSize = prevMax
        return scaleSize 

    def calcScaleResultant(self, resultX, resultY):
        scaleSize = max(abs(resultX), abs(resultY))
        return scaleSize 

    
    #Draws the graph of the vectors
    # Creating plot
    def graphSingleVector(self, vector):
        plotter.title("VectorCalc")

        # Holds vector components
        x = vector.get_x_component()
        y = vector.get_y_component()
        
        #CREATE AND SHOW GRAPH FOR VECTORS
        # Holds origin for graph
        x_origin = [0]
        y_origin = [0]

        # Creating plot
        plotter.quiver(x_origin, y_origin, x, y, angles = 'xy', scale_units= 'xy', scale=1)
         
        # x-lim and y-lim
        plotter.xlim(-1.25 * max(abs(x), abs(y)), 1.25 * max(abs(x) , abs(y)))
        plotter.ylim(-1.25 * max(abs(x), abs(y)), 1.25 * max(abs(x) , abs(y)))

        #Draw and display graph.
        plotter.grid()
        plotter.show()
    
    def graphMultipleVectors(self, vectorList):
        
        print(vectorList.toString())
        lengthList = vectorList.getSize()
        # Holds origin for graph
        origin_points = [0] * lengthList

        # Creates empty list. Will later be filled with the x and y components of vector objects
        x_components = [0] * lengthList
        y_components = [0] * lengthList
        
        #used as index for creating array of x-values.
        vectorCounter = 0

        for vector in vectorList.getVectorList():
            x_components[vectorCounter] = vector.get_x_component() 
            y_components[vectorCounter] = vector.get_y_component() 
            vectorCounter = vectorCounter + 1

        #Scales vector graph to fit largest vector
        scaleSize = self.calcScaleNonresultant(vectorList)

        # Creating plot 
        plotter.quiver(origin_points, origin_points, x_components, y_components, angles = 'xy', scale_units= 'xy', scale=1)
        plotter.title("Graph of Multiple Vectors")

        # x-limit and y-limit of graph that is drawn
        plotter.xlim(-1.25 * max(abs(scaleSize), abs(scaleSize)), 1.25 * max(abs(scaleSize) , abs(scaleSize)))
        plotter.ylim(-1.25 * max(abs(scaleSize), abs(scaleSize)), 1.25 * max(abs(scaleSize) , abs(scaleSize)))


    
        #Draw and display graph.
        plotter.grid()
        plotter.show()


    def graphResultant(self, vectorList):
        
        lengthList = vectorList.getSize()
        # Holds origin for graph
        origin_points = [0]

        # Creates empty list. Will later be filled with the x and y components of vector objects
        x_components = [0]
        y_components = [0]
       
        #Stores resultant values
        x_componentSum = 0 
        y_componentSum = 0    

        #TODO find a way to get the x_componentSum and y_componentSum and pass them to the quiver method
        #I am having trouble with the scope and getting access to these values outside the for loop
        #Calculate resultant
        for vector in vectorList.getVectorList():
            x_componentSum += vector.get_x_component()
            y_componentSum += vector.get_y_component()
       
        #passed as two arrays to quiver for graphing the resultant vector
        x_components[0] = x_componentSum 
        y_components[0] = y_componentSum

        #Scales vector graph to fit largest vector
        scaleSize = self.calcScaleResultant(x_componentSum, y_componentSum)

        # Creating plot 
        plotter.quiver(origin_points, origin_points, x_components, y_components, angles = 'xy', scale_units= 'xy', scale=1)
        plotter.title("Graph of Multiple Vectors")

        # x-limit and y-limit of graph that is drawn
        plotter.xlim(-1.25 * max(abs(scaleSize), abs(scaleSize)), 1.25 * max(abs(scaleSize) , abs(scaleSize)))
        plotter.ylim(-1.25 * max(abs(scaleSize), abs(scaleSize)), 1.25 * max(abs(scaleSize) , abs(scaleSize)))
    
        #Draw and display graph.
        plotter.grid()
        plotter.show()

    def graphEquilibrium(self, vectorList):
        
        lengthList = vectorList.getSize()
        # Holds origin for graph
        origin_points = [0]

        # Creates empty list. Will later be filled with the x and y components of vector objects
        x_components = [0]
        y_components = [0]
       
        #Stores resultant values
        x_componentSum = 0 
        y_componentSum = 0    

        #TODO find a way to get the x_componentSum and y_componentSum and pass them to the quiver method
        #I am having trouble with the scope and getting access to these values outside the for loop
        #Calculate resultant
        for vector in vectorList.getVectorList():
            x_componentSum += vector.get_x_component()
            y_componentSum += vector.get_y_component()
       
        #passed as two arrays to quiver for graphing the resultant vector
        x_components[0] = -x_componentSum 
        y_components[0] = -y_componentSum

        #Scales vector graph to fit largest vector
        scaleSize = self.calcScaleResultant(x_componentSum, y_componentSum)

        # Creating plot 
        plotter.quiver(origin_points, origin_points, x_components, y_components, angles = 'xy', scale_units= 'xy', scale=1)
        plotter.title("Graph of Multiple Vectors")

        # x-limit and y-limit of graph that is drawn
        plotter.xlim(-1.25 * max(abs(scaleSize), abs(scaleSize)), 1.25 * max(abs(scaleSize) , abs(scaleSize)))
        plotter.ylim(-1.25 * max(abs(scaleSize), abs(scaleSize)), 1.25 * max(abs(scaleSize) , abs(scaleSize)))
    
        #Draw and display graph.
        plotter.grid()
        plotter.show()

