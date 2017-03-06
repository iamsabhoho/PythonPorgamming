import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

tx, ty = initial_tx, initial_ty

def horizontal(tx):
    if light_x > initial_tx and tx <= 38:
        return 'E', 1
    elif light_x < initial_tx and tx > 0:
        return 'W', -1
    else:
        return '', 0



#vertical
def vertical(ty):
    if light_y > initial_ty and ty <= 16:
        return 'S', 1
    elif light_y < initial_ty and ty > 0:
        return 'N', -1
    else:
        return '', 0


# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    direction_h, change_h = horizontal(tx)
    direction_v, change_v = vertical(ty)
    print(direction_v + direction_h)
    tx = tx + change_h
    ty = ty + change_v

    # To debug: print("Debug messages...", file=sys.stderr)
    # A single line providing the move to be made: N NE E SE S SW W or NW

