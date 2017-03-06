import turtle

def sqr(sqrlen, tur):
    """
    #draw a tree with turtle
    :param sqrlen: the len of the square
    :param tur:
    :return:
    """
    if sqrlen >= 10:
        return
    else:
        tur.fd(sqrlen)

        sqr(sqrlen-20, tur)

#creates window
myWin = turtle.Screen()
#creates turtle
rp = turtle.Turtle()
#turing left
rp.left(90)
#draw square
sqr(150, rp)
#close the window with a click
myWin.exitonclick()
