import pygame
import random
import math


backgroundColor = (255, 255, 255)
(width, height) = (1000, 400)

class Particle():
    '''
    creates a particle object
    '''

    num_particles = 0

    def __init__(self, x, y, size, angle=math.pi/2, speed=0.5):
        self.x = x
        self.y = y
        self.size = size
        self.color = (0, 55, 165)
        self.thickness = 2
        self.speed = speed
        self.angle = angle # -- going to the right by default
        Particle.num_particles += 1

    def draw(self, screen):
        '''
        draws the particle on the screen
        :return:
        '''
        pygame.draw.circle(screen,
                           self.color,
                           (int(self.x), int(self.y)),
                           self.size,
                           self.thickness)

    def move(self):
        '''
        move the particle given the angle and speed
        :return: None
        '''
        self.x += self.speed * math.sin(self.angle)
        self.y -= self.speed * math.cos(self.angle)

    def bounce(self, height, width):
        '''
        check for particles approacing the walls and bounce them
        :return: None
        '''
        if self.x > width - self.size:
            self.x = 2 * (width - self.size) - self.x
            self.angle = -self.angle

        elif self.x < self.size:
            self.x = 2 * self.size - self.x
            self.angle = -self.angle

        if self.y > height - self.size:
            self.y = 2 * (height - self.size) - self.y
            self.angle = math.pi - self.angle

        elif self.y < self.size:
            self.y = 2 * self.size - self.y
            self.angle = math.pi - self.angle

    def addGarvity(self, gravity):
        anfle, speed = gravity
        self.angle, self.speed = addVectors((self.angle, self.speed), angle, speed)

    def experienced_drag(self, drag=0.9):
        self.speed *= drag

def addVectors(angle1, length1, angle2, length2):
    '''return the sum of two vectors'''

    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y,x)
    length = math.hypot(x,y)
    return (angle, length)

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Particle simulator with OOP')

# -- number of particles
num_particles = 50
# -- particle info
min_size = 10
max_size = 20
gravity = (math.pi/2, 0.0001)
# -- list to store particles
set_particles = list()

for i in range(num_particles):
    size = random.randint(min_size, max_size)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)
    angle = random.uniform(0, 2*math.pi)
    set_particles.append(Particle(x=x, y=y, size=size, angle=angle))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backgroundColor)

    # -- draw the particles
    for par in set_particles:
        par.gravity(gravity=gravity)
        par.move()
        par.bounce(height,width)
        par.draw(screen)

    pygame.display.flip()
