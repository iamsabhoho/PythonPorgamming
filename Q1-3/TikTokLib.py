def displayGrid(grid):
    #prints out grids and values

    print('  ' + grid[1] + '|' + grid[2] + '  |' + grid[3])
    print('___|___|___ ')
    print('  ' + grid[4] + '|' + grid[5] + '  |' + grid[6])
    print('___|___|___')
    print('  ' + grid[7] + '|' + grid[8] + '  |' + grid[9])

    return

def checkWinner(grid, symbol):
    #checking if they are lined up in either horizontal, vertical, or crossed
    if grid[1] == grid[2] == grid[3]:
        result = grid[1]
    elif grid[4] == grid[5] == grid[6]:
        result = grid[4]
    elif grid[7] == grid[8] == grid[9]:
        result = grid[7]

    elif grid[1] == grid[4] == grid[7]:
        result = grid[1]
    elif grid[2] == grid[5] == grid[8]:
        result = grid[2]
    elif grid[3] == grid[6] == grid[9]:
        result = grid[3]

    elif grid[1] == grid[5] == grid[9]:
        result = grid[1]
    elif grid[3] == grid[5] == grid[7]:
        result = grid[3]
    else:
        result = None

    space = 0
    for i in range(0,8):
        if grid[i+1] == ' ':
            space += 1


    if symbol is 'H' and result is 'X':
        return 10
    elif symbol is 'H' and result is 'O':
        return -10
    elif symbol is 'M' and result is 'X':
        return -10
    elif symbol is 'M' and result is 'O':
        return 10
    if space == 0:
            return 0
    return

def playersInput(grid, turn):
    """
    Prompts Players to enter a play and then updates the board
    :return: None
    """
    spot = int(input("This is " + turn + " turn. Please input where you want to place: "))
    print(int(spot))

    if spot == turn:
        grid[spot] = turn
    else:
        print('This spot is taken.')

    return grid

def menu():
    print('This is the tic tac toe. There will be two users at one time.' +
          'each person will get either a "x" or "o" as your symbol. ' +
          ' ' + 'The ')

    #print out whose turns it is: o or x

    return
