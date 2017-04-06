import turtle
import math

def drawTri(tur, len):
    if len>20:
        tri(tur,0.5*len)
    else:
        tur.down()
        tur.fd(0.25*len)
        tur.left(120)
        tur.fd(0.5*len)
        tur.left(120)
        tur.fd(0.5*len)
        tur.left(120)
        tur.fd(0.25*len)

def tri(tur, len):
    """
    #draw triangles with turtle
    :param len: the len of the square
    :param tur:
    :return:
    """

    #right
    tur.up()
    tur.fd(0.25*len)
    tur.down()
    drawTri(tur,len)

    #left
    tur.up()
    tur.backward(0.5*len)
    tur.down()
    drawTri(tur,len)

    #top
    tur.up()
    tur.fd(0.25*len)
    tur.left(90)
    tur.fd(math.sqrt(3)*0.25*len)
    tur.down()
    tur.right(90)
    drawTri(tur,len)

    tur.up()
    tur.right(90)
    tur.fd(math.sqrt(3)*0.25*len)
    tur.left(90)
    tur.down()

#creates window
myWin = turtle.Screen()
#creates turtle
rp = turtle.Turtle()
#draw square
rp.up()
rp.right(90)
rp.fd(200)
rp.left(90)
tri(rp, 500)
#close the window with a click
myWin.exitonclick()
