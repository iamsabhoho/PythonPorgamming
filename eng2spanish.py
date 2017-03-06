import numpy as np
import matplotlib.pyplot as plt

'''eng2spa = {'one': 'uno', 'two': 'dos','three': 'tres','four':'cuatro','five':'cinco',
           'six':'seis','seven':'siete','eight':'ocho','nine':'nueve','ten':'diez'}

user = input('Please enter a number in spanish: ')
x = eng2spa.values()

if user in x:
    print('yes')
else:
    print('no')'''
'''
def generateModel(text):
   model = {}
   for i in range(len(text) - 1):
       fragment = text[i:i+1]
       next_letter = text[i+1]
       if fragment not in model:
           model[fragment] = {}
       if next_letter not in model[fragment]:
           model[fragment][next_letter] = 1
       else:
           model[fragment][next_letter] += 1
   print(model)
   return model

generateModel('abcd')
'''
'''
#print out the scatter plot of the circle
t = [(0.2*x - 10) for x in range(100)]

points = [(x,y) for x in t for y in t if np.sqrt(x**2 + y**2) < 5]

for x, y in points:
    plt.scatter(x,y,marker = 'x', c = 'red')

plt.show()
'''


