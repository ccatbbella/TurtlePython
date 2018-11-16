# project01.py, Yi Xiao Yue (Bella)
from basicShapes import *
import random



def drawTree(height, color):
    ''' 
    This function draws a tree of a given height that consists of a rectangular brown bark and a top comprised of three triangles of a given color stacked on top of each other.
    The bottom left corner of the bark should be at current location of the turtle making no assumptions about the orientation of the turtle.
    After drawing the tree the turtle should be returned to its original position and oriented at 0 degrees 
    All other parameters such as the width of the tree and the length of the bark must be chosen so that the tree is well proportioned: a taller tree is wider and has a thicker and taller bark.
    '''
    #draw tree trunk
    startX = Lucia.xcor()
    startY = Lucia.ycor()   #set up startX and startY variables
    width = (1/3)* height   #set up width variable
    Lucia.up()
    Lucia.goto(startX + (2/5)* width, startY)   #go to left bottom corner of tree trunk
    Lucia.down()
    drawRectangle((1/5)*width, (1/3)*height, 0, "", "brown")  #draw a brown rectangle using startX, startY, and width
    
    #draw tree body
    Lucia.up()
    Lucia.goto(startX, startY + (1/3)*height)
    Lucia.down()    #go to the left corner of the bottom triangle of the tree body
    for i in range(3):     #set up for loop for i = 3
        drawTriangle(width, (1/3)*height, "", color) #draw triangle with base width, and height of one thrid of the tree height
        Lucia.up()  #move up 1/6 * (startY + height)
        Lucia.seth(90)
        Lucia.forward((1/6)*height)
        Lucia.down()
        Lucia.seth(0)

    #return to initial location of the turtle
    Lucia.up() #go to the bottom left of tree trunk
    Lucia.goto(startX + (2/5)*width, startY)
    Lucia.seth(0)  #set angle to east
    
    




def checkTreeHeight():
    Lucia.up()
    Lucia.goto(0,0)
    Lucia.down()
    drawRectangle(100, 200, 0, "red","")
    Lucia.seth(0)
    drawTree(200,"green")
    Lucia.up()
    Lucia.goto(200,200)
    Lucia.down()
    drawRectangle(50, 100, 0, "red","")
    Lucia.seth(0)
    drawTree(100,"green")



def drawForest():
    ''' 
    Draws a collection of trees placed at random locations within a rectangular region
    '''
    
    
    for i in range(10):
        Lucia.up()
        Lucia.seth(0)
        x = -400 + i * 80 + random.randint(-10, 50)
        y = 50 + random.randint(-30, 30)

        Lucia.goto(x,y)
        Lucia.down()
        shadesOfGreen =["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"]
        color = random.choice(shadesOfGreen)
        heightOption = [150, 200, 250]
        height = random.choice(heightOption)
       
        drawTree(height, color)


def drawHut():
    '''
    Draw a brown hut of fixed dimensions purely composed of rectangles
    Use the random module to enhance your drawing by introducing irregularilities in a controlled way
    '''
    #draw body of hut
    for i in range(10):
        drawRectangle(10, 60, 0, 'black', 'brown')
        Lucia.up()
        Lucia.forward(7)
        Lucia.down()     #draw a row of rectangle using for loop

    #move to a central point
    Lucia.up()
    Lucia.backward(34)
    Lucia.left(90)
    Lucia.forward(100)
    Lucia.down()

    #draw top of hut
    for i in range(15):    #draw 15 rectangles rotating around the central point
        drawRectangle(10, 70 + random.randint(-7, 7), 120 + i* 10, 'black', 'brown')   ##tilt????

    #move back to bottom left of body of hut
    Lucia.seth(0)
    Lucia.up()
    Lucia.backward(39)
    Lucia.right(90)
    Lucia.forward(100)
    Lucia.seth(0)

def drawVillage():
    '''
    Draw a sequence of five huts, placed randomly along a horizontal line
    '''
    Lucia.up()
    Lucia.goto(-500, -300)
    for i in range(5):
        Lucia.up()
        x = Lucia.xcor() + 150
        y = -100 + random.randint(-35, 35)
        Lucia.goto(x,y)
        Lucia.down()
        drawHut()



def drawStar(color):
    
    for i in range(5):
        drawTriangle(10, 20,'', color)
        Lucia.seth(i* (-72))
        Lucia.up()
        Lucia.forward(10)
        Lucia.right(72)

def drawManyStars():
    Color = ['#fe6f5e', '#ffff99', '#99badd', '#bf94e4', '#536872', '#a52a2a', '#ff0040', '#b2beb5', '#b2ffff']
   

    for i in range(12):
        starColor = random.choice(Color)
        Lucia.up()
        x = -500 + i * 80 + random.randint(0, 60)
        y = 300 + random.randint(-50,30)

        Lucia.goto(x,y)
        Lucia.down()
        drawStar(starColor)
        
 if __name__=="__main__":
    
    drawForest()
    drawVillage()
    drawManyStars()
    
