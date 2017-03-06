import pygame as pg
import sys
import myLib
from pygame.locals import *

#initialize the pygame lib
pg.init()
#sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
#title
pg.display.set_caption('State Machine')
#the clock will be used to control how fast the screen updates
clock = pg.time.Clock()

#read the game images: sprites
redLight = pg.image.load('red.jpg')
yellowLight = pg.image.load('yellow.jpg')
greenLight = pg.image.load('green.jpg')
offLight = pg.image.load('off.jpg')

#dictionary for characters
traffic = {'red': redLight,
           'green': greenLight,
           'yellow': yellowLight,
             'off': offLight,
             'pos_x': 80,
             'pos_y':0
           }

state = {'state': 'off', 'counter': 0}

while True:

    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
        keys = pg.key.get_pressed()

    if keys[pg.K_SPACE]:
        state['state'] = 'red' if state['state'] is 'off' else 'off'

    window.fill((255,255,255))
    pg.draw.line(window, (0, 0, 0), (0, 200), (200, 200))
    traffic_rect = pg.Rect(traffic['pos_x'], traffic['pos_y'], 10, 10)

    if state['state'] is 'red':
        red_rect = pg.Rect(traffic['pos_x'] + traffic['off'], 50, 50)
        window.blit(redLight, red_rect)
        #transition
        state['counter'] += 1
        if state['counter'] >= 10:
            state['state'] = 'green'
            state['counter'] = 0

    elif state['state'] is 'green':
        green_rect = pg.Rect(traffic['pos_x'] + traffic['off'], 50, 50)
        window.blit(greenLight, green_rect)
        #transition
        state['counter'] += 1
        if state['counter'] >= 10:
            state['state'] = 'yellow'
            state['counter'] = 0

    elif state['state'] is 'yellow':
        yellow_rect = pg.Rect(traffic['pos_x'] + traffic['off'], 50, 50)
        window.blit(yellowLight, yellow_rect)
        #transition
        state['counter'] += 1
        if state['counter'] >= 10:
            state['state'] = 'red'
            state['counter'] = 0

    #replace rect by image
    window.blit(traffic['off'], traffic_rect)

    # --- update the screen
    pg.display.flip()

    # --- limit to 60 frames per second
    clock.tick(10)


pg.quit()
