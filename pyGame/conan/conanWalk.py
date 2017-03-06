import pygame as pg
import sys

from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('walking machine')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# load images
walk_1 = pg.image.load('walk1.png')
walk_2 = pg.image.load('walk2.png')
walk_3 = pg.image.load('walk3.png')
wait = pg.image.load('wait_f.png')
left1 = pg.image.load('left1.png')
left2 = pg.image.load('left2.png')
left3 = pg.image.load('left3.png')
back1 = pg.image.load('back1.png')
back2 = pg.image.load('back2.png')
back3 = pg.image.load('back3.png')
right1 = pg.image.load('right1.png')
right2 = pg.image.load('right2.png')
right3= pg.image.load('right3.png')




conan = {
    'pos_y': int(winSize[1]/2),
    'pos_x': int(winSize[0]/2),
    'wait': wait,
    'walk1': walk_1,
    'walk2': walk_2,
    'walk3': walk_3,
    'left1': left1,
    'left2': left2,
    'left3': left3,
    'back1': back1,
    'back2': back2,
    'back3': back3,
    'right1': right1,
    'right2': right2,
    'right3': right3,

    }

# --dictionary for the state machine
state = {'state':'wait', 'param':{}, 'image':'wait'}

speed = 10

while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
    keys = pg.key.get_pressed()

    window.fill((255, 255, 255))

    if state['state'] is 'wait':
        # -- output
        state['image'] = 'wait'
        # -- transition
        if keys[K_DOWN]:
            state['state'] = 'walk'
            state['param'] = {'time':0}
        if keys[K_UP]:
            state['state'] = 'back'
            state['param'] = {'time':0}
        if keys[K_RIGHT]:
            state['state'] = 'right'
            state['param'] = {'time':0}
        if keys[K_LEFT]:
            state['state'] = 'left'
            state['param'] = {'time':0}

    elif state['state'] is 'walk':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'walk' + str(n)
        conan['pos_y'] += speed

        # -- transition
        if keys[K_DOWN]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'left':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'left' + str(n)
        conan['pos_x'] -= speed

        # -- transition
        if keys[K_LEFT]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    elif state['state'] is 'back':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'back' + str(n)
        conan['pos_y'] -= speed

        # -- transition
        if keys[K_UP]:
            state['param']['time'] += 1

    elif state['state'] is 'right':
        # -- output
        t = state['param']['time']
        n = t%3 + 1
        state['image'] = 'right' + str(n)
        conan['pos_y'] -= speed

        # -- transition
        if keys[K_UP]:
            state['param']['time'] += 1
        else:
            state['state'] = 'wait'

    conan_rect = pg.Rect(conan['pos_x'], conan['pos_y'], 50, 50)
    image = state['image']
    window.blit(conan[image], conan_rect)

    # --- Go ahead and update the screen with what we've drawn.
    pg.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(10)
