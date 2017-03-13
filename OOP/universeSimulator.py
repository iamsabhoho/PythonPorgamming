import pygame
import random
import math


backgroundColor = (0, 0, 0)
(width, height) = (1000, 400)

class Particle():
    '''
    creates a particle object
    '''

    num_particles = 0

    def __init__(self, x, y, size, angle=math.pi/2, speed=1.0, mass=1.0):
        self.x = x
        self.y = y
        self.size = size
        self.color = (255, 255, 255)
        self.thickness = 0 # --- so it prints the whole circle
        self.speed = speed
        self.angle = angle # --- going to the right by default
        self.mass = mass
        Particle.num_particles += 1

    def attract(self, other):
        """
        gravitational force
        :param other: another particle to whom we attract
        :return:
        """
        dx = (self.x - other.x)
        dy = (self.y - other.y)
        distance = (dx ** 2 + dy ** 2) ** (0.5)
        force = self.mass * other.mass / (distance ** 2)

        # --- check for colliding particles
        if distance < self.size + other.size:
            return True # --- meaning it collides

        # --- angle
        angle = math.atan2(dy, dx)
        # --- newton's law
        self.accelerate(angle + math.pi/2, force/self.mass)
        other.accelerate(angle - math.pi/2, force/other.mass)



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

    def accelerate(self, angle, speed):
        """
        accelerates the particle by the given angle and speed

        :param angle:
        :param speed:
        :return:
        """
        self.angle, self.speed = addVectors(self.angle, self.speed, angle, speed)

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
        angle, speed = gravity
        self.angle, self.speed = addVectors((self.angle, self.speed), angle, speed)

    def experience_drag(self, drag=0.9):
        self.speed *= drag

def addVectors(angle1, length1, angle2, length2):
    '''return the sum of two vectors'''

    x = math.sin(angle1) * length1 + math.sin(angle2) * length2
    y = math.cos(angle1) * length1 + math.cos(angle2) * length2

    angle = 0.5 * math.pi - math.atan2(y,x)
    length = math.hypot(x,y)
    return (angle, length)

def collide(p1, p2):
    """
    combines two colliding particles into one bigger
    :param p1:
    :param p2:
    :return:
    """

    total_mass = p1.mass + p2.mass
    total_size = p1.size + p2.size

    # --- position of the new particle
    p1.x = (p1.x * p1.mass + p2.x * p2.mass) / total_mass
    p1.y = (p1.y * p1.mass + p2.y * p2.mass) / total_mass

    # ---
    (angle, speed) = addVectors(p1.angle, p1.speed * p1.mass / total_mass,
                                p2.angle, p2.speed * p2.mass / total_mass)

    p1. speed = speed
    p1.angle = angle
    p1.mass = total_mass
    p1.size = total_size
    p1.collided_with = p2

def calculateSize(mass):
    return 0.5 * mass ** (0.5)


screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Particle simulator with OOP')

# -- number of particles
num_particles = 50
# -- particle info
min_mass = 1
max_mass = 4
#gravity = (math.pi/2, 0.0001)
# -- list to store particles
set_particles = list()

for i in range(num_particles):
    mass = min_mass + 0.5 * max_mass * random.random()

    size = int(calculateSize(mass))

    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    angle = random.uniform(0, 2*math.pi)

    set_particles.append(Particle(x=x,
                                  y=y,
                                  size=size,
                                  angle=angle,
                                  speed = 0.0,
                                  mass = mass))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(backgroundColor)
    particle_to_remove = []

    for i, p1 in enumerate(set_particles):

        for p2 in set_particles[i+1:]:
            if p1.attract(p2):
                collide(p1, p2)

        if p1.size > 5:
            p1.color(225, 225, 0)

        if 'collided_with' in p1.__dict__:
            particle_to_remove.append(p1.collided_with)
            p1.size = calculateSize(p1.mass)
            del p1.__dict__['collided_with']

        p1.experience_drag(drag = 0.99)
        p1.move()
        p1.draw(screen)

    for p in particle_to_remove:
        if p in set_particles:
            set_particles.remove(p)

    pygame.display.flip()
