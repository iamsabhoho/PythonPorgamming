#Create an script that receives an integer n via user input, and return True if it is within 10 of 100 or 200. Make sure to validate the data type of the user’s input.

import sys

valueF = 1
while valueF > 0:
    valueF = float(input("Please enter a value:"))
    valueI = int(valueF)

    if valueF == valueI:
        if 10<= int(valueI) <= 100:
            print('True')
        elif int(valueI) == 200:
            print('True')
        else:
            print('False')
    else:
        print('False, vI != vF')
print('The End...')

