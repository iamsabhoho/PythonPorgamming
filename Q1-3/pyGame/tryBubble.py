import pygame as pg
import sys, math
from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (1000, 400)
window = pg.display.set_mode(winSize)
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()

# --- default particle
def particle(x=10, y=10, size=15, colour=(0, 0, 255), thickness=2, speed=0, angle=math.pi/2):
    return {'x': x, 'y': y, 'size': size, 'colour': colour, 'thickness': thickness, 'speed': speed, 'angle': angle}


def move(particle):
    """
        move particle by calculating velocity vector
    :param particle:
    :return: particle
    """
    angle = particle['angle']
    speed = particle['speed']
    particle['x'] += math.sin(angle) * speed
    particle['y'] -= math.cos(angle) * speed

    return particle

def draw(particle):
    """
        draws particle in the screen
    :param particle:
    :return: None
    """
    # --- de-encapsulate
    colour = particle['colour']
    size = particle['size']
    thickness = particle['thickness']
    x = particle['x']
    y = particle['y']
    pg.draw.circle(window, colour, (int(x), int(y)), size, thickness)

# --- let's create a single particle
particle = particle(x=200, y=100, thickness=0, size=20, colour=(255, 0, 0))
# --- flag variable to detect when the mouse was pressed

mouse_click = False

while True:  # main game loop
    for event in pg.event.get():
        if event.type is QUIT:
            pg.quit()
            sys.exit()
        # --- Here the mouse x and y position is captured when the mouse left button is pressed
        elif event.type == pg.MOUSEBUTTONDOWN:
            # --- here the mouse's position is read
            (mouseX, mouseY) = pg.mouse.get_pos()
            mouse_click = True
        elif event.type == pg.MOUSEBUTTONUP:
            # --- if the button is released then clear flab
            mouse_click = False

    # --- Draw sprites
    window.fill((255, 255, 255))

    if mouse_click:
        # --- Get the mouse position and move particle in that direction
        dx = mouseX - particle['x']
        dy = mouseY - particle['y']
        # --- dx, dy is where the particle should move to
        particle['angle'] = 0.5*math.pi + math.atan2(dy, dx)
        # --- constant speed
        particle['speed'] = 2.0

    particle = move(particle)
    draw(particle)

    # --- update the screen with what we've drawn.
    pg.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(100)
