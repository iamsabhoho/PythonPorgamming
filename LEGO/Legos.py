import numpy as np #libary of functions
import math as m #math fucntions
import matplotlib.pyplot as plt #for plotting points on graph

countBricks = 0
countBeams= 0

#read file
legos = np.loadtxt('Legos2.txt',delimiter=',')

#beams: (7,4)
def beams(x,y):
    distance = m.sqrt(x**2 + y**2)
    return distance

#bricks: (3,5)
def bricks(x,y):
    distance = m.sqrt(x**2 + y**2)
    return distance

#comparing distance for beams and bricks from the text file
for x, y in legos:
    if beams(x, y) < bricks(x, y):
        countBeams += 1
        plt.scatter(x, y, color = "red")

    else:
        countBricks += 1
        plt.scatter(x, y, color = "blue")

plt.show()

beamlist = [(x, y) for x, y in legos if beams(x, y) < bricks(x, y)]
bricklist = [(x, y) for x, y in legos if beams(x, y) > bricks(x, y)]

print("Beams: %r" %countBeams)
print("Bricks: %r" %countBricks)

