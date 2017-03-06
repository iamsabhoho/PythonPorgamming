#Write a function that returns the elements on odd positions in a list.

list = [1,2,3,4,5]

def position():
    for i in range(len(list)):
        if i%2 == 0:
            print(list[i])

    return i

position()
