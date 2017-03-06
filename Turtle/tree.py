import turtle

def tree(tur, branch, length):
    """

    :param tur:
    :param branch:
    :param length:
    :return:
    """
    if branch is not 1:
        tur.write(length)
        tur.fd(length)
        tur.right(20)
        tree(length-15, tur, branch-1)
        tur.left(40)
        tree(length-15, tur, branch-1)
        tur.right(20)
        tur.backward(length)


#creates window
myWin = turtle.Screen()
#creates turtle
rp = turtle.Turtle()
#draw square
tree(rp, 10, 100)
#close the window with a click
myWin.exitonclick()
