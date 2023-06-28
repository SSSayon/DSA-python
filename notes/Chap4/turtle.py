# from turtle import Turtle

# t = Turtle()
# myWin = t.getscreen()

# def drawTree(Turtle: t, branch_len):
#     if branch_len >= 5:
#         t.forward(branch_len)
#         t.right(20)
#         drawTree(t, branch_len - 20)
#         t.left(40)
#         drawTree(t, branch_len - 20)
#         t.right(20)
#         t.backward(branch_len)

# t.left(90)
# drawTree(t, 100)
# myWin.exitonclick()

import turtle
def drawTriangle(points, color, myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1])
    myTurtle.goto(points[2])
    myTurtle.goto(points[0])
    myTurtle.end_fill()

def getMid(p1, p2):
    return ( (p1[0]+p2[0]) /2, (p1[1] + p2[1]) / 2)

def sierpinski(points, degree, myTurtle):
    colormap = ['blue', 'red', 'green', 'yellow']
    drawTriangle(points, colormap[degree], myTurtle)
    if degree > 0:
        sierpinski([points[0], \
                        getMid(points[0], points[1]), \
                        getMid(points[0], points[2])], \
                    degree-1, myTurtle)
        sierpinski([points[1], \
                        getMid(points[0], points[1]), \
                        getMid(points[1], points[2])], \
                    degree-1, myTurtle)
        sierpinski([points[2], \
                        getMid(points[2], points[1]), \
                        getMid(points[0], points[2])], \
                    degree-1, myTurtle)

turtle.setup(750, 750)
myTurtle = turtle.Turtle()
myWin = myTurtle.getscreen()
myPoints = [(-500, -250), (0, 500), (500, -250)]
sierpinski(myPoints, 3, myTurtle)
myWin.exitonclick()