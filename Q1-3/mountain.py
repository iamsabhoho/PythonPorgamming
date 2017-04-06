import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


#insertion sort
def insertionSort(items):
    """
    insertion sorting
    second method to sort the occurence of the words
    :param items:
    :return:
    """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    print(items)
    return items

# game loop
while True:
    mountain_h = []
    for i in range(8):
        mountain_h.append(int(input()))  # represents the height of one mountain.

    # Write an action using print
    print(mountain_h, file=sys.stderr)
    # To debug: print("Debug messages...", file=sys.stderr)

    #sort the height of the mountains


    # The index of the mountain to fire on.
    print('0')
    for j in range(0,8):
        print(j+1)




