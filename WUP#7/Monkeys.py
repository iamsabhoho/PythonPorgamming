#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling (True/False: Boolean type). We are in trouble if they are both smiling or if neither of them is smiling. Create a script that receives the two parameters in the console and return “We are in trouble” if we are in trouble, otherwise “We are fine”. Make sure of validating the parameters’ data type.


import sys

print('The arguments passed were: ')

#a_monkey
if int(sys.argv[1]) == 0:
    a = print('Monkey A is not smiling')
else:
    a = print('Monkey A is smiling')

#b_monkey
if int(sys.argv[2]) == 0:
    b = print('Monkey B is not smiling')
else:
    b = print('Monkey B is smiling')

#results
if int(sys.argv[1]) == int(sys.argv[2]):
    print("We are in trouble.")
else:
    print("We are fine.")
