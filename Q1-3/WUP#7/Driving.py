#You are driving a little too fast, and a police officer stops you. Write an script that computes the result as “no ticket”, “small ticket”, and “big ticket”. If speed is 60 or less, the result is “no ticket”. If speed is between 61 and 80 inclusive, the result is “small ticket”. If speed is 81 or more, the result is “big ticket”. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases. The input of the script in your speed and a boolean variable that indicates if it is your birthday.

import sys

print('The arguments passed were(birthday?/speed?): ')
print(sys.argv)

birthday = str(sys.argv[1])
speed = float(sys.argv[2])

#see if it is the driver's birthday
if birthday == str('yes'): 
    if 0 <= float(speed) <= 65:
        print('No ticket.')
    elif 66 <= float(speed) <= 85:
        print('Small ticket.')
    elif 86 <= float(speed):
        print('Big ticket.')
else: 
    if 0 <= float(speed) <= 60:
        print('No ticket.')
    elif 61 <= float(speed) <= 80:
        print('Small ticket.')
    elif 81 <= float(speed):
        print('Big ticket.')
