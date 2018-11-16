#lab03.py, Yi Xiao Yue(Bella)
import turtle
import math
Lucia = turtle.Turtle()
Lucia.shape("turtle")
Lucia.speed(-10)
Lucia.width(4)
def drawRectangle_1():
    """
    draw a rectangle with width 50 and height 100. Use a turtle called Lucia to create the drawing
    """
    Lucia.color("green","yellow")  # Sets the pen color to green and fill color to yellow
    Lucia.seth(90) # Set the initial orientation of the turtle to 0 degrees
    Lucia.begin_fill()
    Lucia.forward(50)    # Move the turtle forward by 50 units in the direction that it was pointing
    Lucia.left(90)       # Turn the turtle left by 90 degrees relative to the direction it was pointing
    Lucia.forward(100)   # Move the turtle forward by 100 units
    Lucia.left(90)
    Lucia.forward(50)
    Lucia.left(90)
    Lucia.forward(100)
    Lucia.left(90)       # Make sure the turtle is oriented back to its initial orientation
    Lucia.end_fill()
def drawRectangle_2():
    """
    draw a rectangle with width 50, height 100, tilt 0, pen color green and fill color yellow . Use a turtle called t to create the drawing
    """

    # Calculate the coordinates for the four corners of the rectangle
    x1 = Lucia.xcor()
    y1 = Lucia.ycor()
    x2 = x1 + 50
    y2 = y1
    x3 = x2
    y3 = y2 + 100
    x4 = x1
    y4 = y1 + 100
    Lucia.color("green","yellow")   # set the pen and fill colors
    Lucia.begin_fill()
    # Command the turtle to visit the four corners in order
    Lucia.goto(x2, y2)
    Lucia.goto(x3, y3)
    Lucia.goto(x4, y4)
    Lucia.goto(x1, y1)

    Lucia.end_fill()

def drawRectangle_3():
    """
    draw a rectangle with width 50, height 100, tilt 0, pen color green and fill color yellow . Use a turtle called t to create the drawing
    """

    # Calculate the coordinates for the four corners of the rectangle

    x1 = Lucia.xcor()
    y1 = Lucia.ycor()

    fourCorners = [(x1 + 50, y1), (x1 + 50, y1 + 100), (x1, y1 + 100), (x1, y1)]
    
    Lucia.color("green", "yellow")
    Lucia.begin_fill()
    
    Lucia.goto(fourCorners[0][0], fourCorners[0][1])
    Lucia.goto(fourCorners[1][0], fourCorners[1][1])
    Lucia.goto(fourCorners[2][0], fourCorners[2][1])
    Lucia.goto(fourCorners[3][0], fourCorners[3][1])

    Lucia.end_fill()

def drawRectangle(width, height, tilt, penColor, fillColor):
    """
    draw a rectangle with a given width, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner, and the bottom side tilted by an angle tilt (specified in degrees)
    relative to the horizontal axis. After the rectangle is drawn, the turtle should return to its original position with an orientation of 0 degrees with respect to the x-axis.
    Use a turtle called t to create the drawing
    """
    Lucia.color(penColor,fillColor)
    Lucia.seth(tilt)
    Lucia.begin_fill()
    for i in range(2):
        Lucia.forward(width)
        Lucia.left(90)
        Lucia.forward(height)
        Lucia.left(90)
    Lucia.end_fill()


def drawTwoRectangles():
    Lucia.left(180)
    Lucia.up()
    Lucia.forward(500)
    Lucia.down()
    drawRectangle( 50, 100, 0, "red", "") 

    # Move the turtle right by 100 units without leaving a trail

    Lucia.up()     
    Lucia.forward(100)
    Lucia.down()
    drawRectangle( 100, 150, 22, "green", "yellow")


def drawTriangle(base, height, penColor, fillColor):
    """
    draw a triangle with a given base, height, penColor and fillColor,
    with the current location of the turtle being the 
    lower left corner. The base of the triangle should be at 0 degrees with respect to the x-axis. 
    Do not assume anything about the initial orientation of the turtle. 
    The final orientation of the turtle should be 0 degrees with respect to the x-axis. 
    Use a turtle called Lucia to create the drawing
    """

    # Insert code to draw the triangle

    Lucia.color(penColor,fillColor)
    Lucia.begin_fill()
    Lucia.forward(base)
    angle1AsRadian = math.atan(2*height/base)
    angle1AsDegree = math.degrees(angle1AsRadian)
    Lucia.left(180 - angle1AsDegree)
    Lucia.forward(math.sqrt(height**2 + (.5*base)**2))
    Lucia.left(2*angle1AsDegree)
    Lucia.forward(math.sqrt(height**2 + (.5*base)**2))
    
    Lucia.end_fill()

def drawTwoTriangles():
    """ Draws two non overlapping triangles with different sizes and colors
    """

    drawTriangle(200,100,"blue","pink")
    Lucia.up()
    Lucia.forward(220)
    Lucia.down()
    drawTriangle(100,200,"grey","blue")
    Lucia.seth(0)


if __name__=="__main__":
    drawTwoTriangles()

    drawTwoRectangles()



