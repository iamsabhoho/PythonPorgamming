def ptri(n, item):
    """

    :param n: level
    :param item:
    :return:
    """
    print()
    r = []
    item.insert(0, 0)
    item.append(0)
    if n == 0:
        return
    else:
        for i in range(len(item)-1):
            r.append(item[i] + item[i+1])
        for element in r:
            print(str(element) + ' ', end='')
        ptri(n-1, r) #so the termination will eventually happen


def pascal(n):
    print('1', end='')
    ptri(n, [1])


pascal(5)

