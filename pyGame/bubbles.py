import pygame as pg
import sys
import random
import math
from pygame.locals import *

# initialize the pygame library
pg.init()
# sets the size of the window
winSize = (800, 700)
window = pg.display.set_mode(winSize)
# title
pg.display.set_caption('Bubbles')
# The clock will be used to control how fast the screen updates
clock = pg.time.Clock()


def randomPosition():
    """
    Generates random coordinates for particles
    """
    x = int(random.randint(0, 399)/20)*20
    y = int(random.randint(0, 299)/20)*20

    return x, y

def userBubbles():
    """
    ask the user for the amount of particles they want
    :param
    :return: amount that user input
    """
    amount = input('How many particles would you like? ')

    return amount

def particle(x = 10, y = 10, size = 15, colour = (0, 0, 225), thickness = 2, speed = 0, angle = math.pi/2):
    """
    create particles
    :param x:
    :param y:
    :param size:
    :param colour:
    :param thickness:
    :param speed:
    :param angle:
    :return:
    """

    return{'x':x, 'y':y, 'size':size, 'colour':colour, 'thickness':thickness, 'speed': speed, 'angle':angle}

def draw(particle):

    colour = particle['colour']
    size = particle['size']
    thickness = particle['thickness']

    x = particle['x']
    y = particle['y']

    pg.draw.circle(window, colour, (int(x), int(y)), size, thickness)



def new_particles(n = 50):
    group_particle = []
    for i in range(n):
        size = random.randint(10, 20)
        x = random.randint(size, winSize[0] - size)
        y = random.randint(size, winSize[1] - size)
        speed = random.random()
        angle = random.uniform(0, math.pi*2)
        colour = (random.randint(0,225), random.randint(0,225),0)
        group_particle.append(particles(x=x, y=y, size=size, speed=speed, angle=angle))

def add_vectors(vector1, vector2):
    """
    fucntion to add two vectors
    :param vector1: tuple (angle, mag)
    :param vector2: tuple (angle, mag)
    :return vector: tuple (angle, mag)
    """
    angle1, mag1 = vector1
    angle2, mag2 = vector2
    x = math.sin(angle1)*mag1 + math.sin(angle2)*mag2
    y = math.cos(angle1)*mag1 + math.cos(angle2)*mag2
    mag = math.hypot(x,y)
    angle = 0.5*math.pi - math.atan2(y,x)

    return angle, mag

def move(particle):
    angle = particle['angle']
    speed = particle['speed']

    particle['x'] += math.sin(angle) * speed
    particle['y'] -= math.cos(angle) * speed

    return particle

def bounce(particle):

    x = particle['x']
    y = particle['y']
    size = particle['size']
    angle = particle['angle']
    width = winSize[0]
    height = winSize[1]

    if x > width - size:
        x = 2*(width-size) - x
        angle = -angle

    elif x < size:
        x = 2*size - x
        angel = -angle

    if y > height - size:
        y = 2*(height - size) - y
        angle = math.pi - angle

    elif y < size:
        y - 2*size - y
        angle = math.pi - size

    particle['x'] = x
    particle['y'] = y
    particle['angle'] = angle

    return particle




mouse_click = False

#game loop
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
