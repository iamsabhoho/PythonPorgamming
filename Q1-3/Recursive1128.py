import turtle
import colorsys
###################Library################
def drawcircle(x, y, radius, t):
    """

    :param x: the position of x on the coordinate
    :param y: the position of y on the coordinate
    :param radius: the r of the circles
    :param t: turtle
    :return: none
    """
    moveturtle(x, y-radius)
    #pen color
    (r, g, b) = colorsys.hsv_to_rgb(float(radius) / 150, 1.0, 1.0)
    t.pencolor(r, g, b)
    #draw circle
    t.circle(radius)
    #return to the initial position
    moveturtle(x, y)
    #smaller circles
    if radius > 10:
       drawcircle(x+radius, y , radius/2, t)
       drawcircle(x-radius, y , radius/2, t)
    return

def moveturtle(x, y):
    """

    :param x: position of the x on the coordinate
    :param y: position of the y on the coordinate
    :return: none
    """
    t.up()
    t.setposition(x, 2*y)
    t.down()




#######################################

t = turtle.Turtle()
t.pensize(2)
moveturtle(-50, 0)
myWin = turtle.Screen()
drawcircle(x=1, y=100, radius=90,t=t)
myWin.exitonclick()
