import turtle

myTurtle = turtle.Turtle()
myWindow = turtle.Screen()
myTurtle.speed(10)

def spiral(side):
    if side > 0:
        myTurtle.forward(side)
        myTurtle.right(90)
        spiral(side-5)

spiral(100)
myWindow.exitonclick()
