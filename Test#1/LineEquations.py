#Points
c1x = int(input('Please enter a value for x: '))
c1y = int(input('Please enter a vale for y: '))
c2x = int(input('Please enter another value for x: '))
c2y = int(input('Please enter another value for y: '))

#Slope
s = (c2y - c1y)/ (c2x - c1x)
print('The slope is: ' + str(s))

#Ax + By = C
A = s * (-1)
C = c1y - (s * c1x)
print('The standard form is: ' + str(A) + ' x + y = ' + str(C))

#y = mx + b
b = c1y - (s * c1x)
print('The slope-intercept is: y = ' + str(s) + ' x + ' + str(b))

#y - y1 = m(x - x1)
x = c1x * (-1)
y = c1y * (-1)
if(y >= 0 and x >= 0):
    print('The point-slope form is: y - ' + str(y) + ' = ' + str(s) +'( x -  ' + str(x) + ' )')
elif(y < 0 and x < 0):
    print('The point-slope form is: y ' + str(y) + ' = ' + str(s) + '( x ' + str(x) + ')')
elif(y >= 0 and x < 0):
    print('The point-slope form is: y -  ' + str(y) + ' = ' + str(s) + '( x ' + str(x) + ')')
else:
    print('The point-slope form is: y ' + str(y) + ' = ' + str(s) + '( x -  ' + str(x) + ' )')

