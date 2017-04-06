import pygame as pg
import sys
from pygame.locals import *
import random

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (400, 300)
window = pg.display.set_mode(winSize)
cellSize = 20
# title
pg.display.set_caption('My first game')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()
# Set start point.
wormCoords = [{'x': 5, 'y': 5},
              {'x': 5, 'y': 4},
              {'x': 5, 'y': 3}]


startscreen = pg.image.load('start.jpg')
endscreen = pg.image.load('gameover.jpg')

def drawGrid(win, winSize, cellSize, color):
    """
    Draws the grid for the game
    :param win: identifier of the window
    :param winSize: winSize (width,height)
    :param cellSize:
    :param color:
    """
    for x in range(0, winSize[0], cellSize):  # draw vertical lines
        pg.draw.line(win, color, (x, 0), (x, winSize[1]))
    for y in range(0, winSize[1], cellSize):  # draw horizontal lines
        pg.draw.line(win, color, (winSize[0], y), (0, y))


def drawWorm(win, wormCoor, cellSize, wormColor):
    for c in wormCoor:
        x = c['x'] * cellSize
        y = c['y'] * cellSize
        wormSegmentRect = pg.Rect(x, y, cellSize, cellSize)
        pg.draw.rect(win, wormColor, wormSegmentRect)

def drawApple(win, appleSize, appleColor, x, y):
    """
    Draws the apple in the game that displayed randomly
    """
    appleRect = pg.Rect(x, y, appleSize, appleSize)
    pg.draw.rect(win, appleColor, appleRect)


def randCoord():
    """
    Generates random coordinates
    """
    x = int(random.randint(0, 399)/20)*20
    y = int(random.randint(0, 299)/20)*20

    return x, y

direction = 'right'
apple_x, apple_y = randCoord()

def scoring(score):
    """
    scoring for the snake getting an apple
    :param score:
    :return:
    """
    return score

while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        direction = 'left'
    if keys[pg.K_RIGHT]:
        direction = 'right'
    if keys[pg.K_UP]:
        direction = 'up'
    if keys[pg.K_DOWN]:
        direction = 'down'

    if direction is 'up':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] - 1}
    elif direction is 'down':
        newHead = {'x': wormCoords[0]['x'], 'y': wormCoords[0]['y'] + 1}
    elif direction is 'left':
        newHead = {'x': wormCoords[0]['x'] - 1, 'y': wormCoords[0]['y']}
    else:
        newHead = {'x': wormCoords[0]['x'] + 1, 'y': wormCoords[0]['y']}

    wormCoords.insert(0, newHead)

    #del wormCoords[-1]  # remove worm's tail segment

    window.fill((255, 255, 255))
    drawGrid(window, winSize, cellSize, (40, 40, 40))
    drawWorm(window, wormCoords, cellSize, (0, 200, 0))
    drawApple(window, cellSize, (0, 255, 0), apple_x, apple_y)

    if newHead['x']*20 != apple_x or newHead['y']*20 != apple_y:
        del wormCoords[-1]  # remove worm's tail segment
        wormCoords.insert(0, newHead)
    else:
        apple_x, apple_y = randCoord()
        wormCoords.insert(0, newHead)


    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
