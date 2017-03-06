import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


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
    maxvalue = max(mountain_h)
    print(mountain_h.index(maxvalue))
