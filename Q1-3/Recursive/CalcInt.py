def calc(x):
    """
    This function finds the number in the blank
    :param x:
    :return:
    """

    if x == 1:
        return 1
    else:
        return (x*calc(x-1))

num = 4
print('The ____ number ' + str(num) + ' is ' + str(calc(num)))
