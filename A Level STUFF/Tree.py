import turtle

def tree(branchLen):
    if branchLen > 5:
        t.shapesize(2)
        t.forward(branchLen)
        t.right(30)
        tree(branchLen-15)
        t.left(60)
        tree(branchLen-15)
        t.right(30)
        t.backward(branchLen)
    else:
        t.color("purple")
        t.stamp()

t = turtle.Turtle()
myWindow = turtle.Screen()

t.left(90)
t.up()
t.backward(300)
t.down()


tree(90)

myWindow.exitonclick()