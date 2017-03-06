import sys
import pygame
import gameLib

# initialize pygame library
pygame.init()

# open a new window
windowSize = (700,500)
screen = pygame.display.set_mode(windowSize)
sizeCell = 20

# title
pygame.display.set_caption("The snake game")

# starting point
snakeCoordinate = [{'x':5, 'y':5}, {'x':5, 'y':4}, {'x':5, 'y':3}]
direction = ''

# The loop will carry on until the user exit the game
carryOn = True

# The clock will  be used to control how fast the screen updates
clock = pygame.time.Clock()

def grid(windowSize, screen, color, sizeCell):

    numRows = windowSize[0] / sizeCell
    numColumns = windowSize[1] / sizeCell

    for y in range(0, windowSize[1], sizeCell):
        pygame.draw.line(screen, (0, 0, 0), (0, y), (windowSize[0], y))

    for x in range(0, windowSize[0], sizeCell):
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (x, windowSize[1]))



def snake(screen, wormCoordinate, sizeCell, snakeColor):
    for i in wormCoordinate:
        x = i['x'] * sizeCell
        y = i['y'] * sizeCell
        wormHead = pygame.Rect(x, y, sizeCell, sizeCell)
        pygame.draw.rect(screen, snakeColor, wormHead)

# -------------- Main Program Loop --------------
while carryOn:

    ch = gameLib.getkey()
    print(ch + ' pressed')
    if ord(ch) is 27:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get(): # user did something
        if event.type == pygame.QUIT: # if user click close
            carryOn = False # flag that we are done so we exit
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        direction = 'right'
    if keys[pygame.K_LEFT]:
        direction = 'left'
    if keys[pygame.K_UP]:
        direction = 'up'
    if keys[pygame.K_DOWN]:
        direction = 'down'

    if direction == 'right':
        newHeadPosition = {'x': snakeCoordinate[0]['x'] + 1, 'y': snakeCoordinate[0]['y']}
    elif direction == 'left':
        newHeadPosition = {'x': snakeCoordinate[0]['x'] - 1, 'y': snakeCoordinate[0]['y']}
    elif direction == 'up':
        newHeadPosition = {'x':snakeCoordinate[0]['x'], 'y':snakeCoordinate[0]['y'] - 1}
    else:
        newHeadPosition = {'x': snakeCoordinate[0]['x'], 'y': snakeCoordinate[0]['y'] + 1}

    snakeCoordinate.insert(0, newHeadPosition) # new head's position into the list
    del snakeCoordinate[-1] # remove the tail

    '''
    # snake cannot touch the wall
    if snakeCoordinate[0][0] == 0 or snakeCoordinate[0][0] == 19 or snakeCoordinate[0][1] == 0 or snakeCoordinate[0][1] == 59:
        break
'''
    # --- drawing code should go here
    # first, clear the screen to WHITE
    screen.fill((255,255,255))
    grid(windowSize, screen, (0, 0, 0), sizeCell)
    snake(screen, snakeCoordinate, sizeCell, (255, 0, 0))

    # --- update the screen
    pygame.display.flip()

    # --- limit to 60 frames per second
    clock.tick(10)



pygame.quit()
