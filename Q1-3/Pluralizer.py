#this program converts single object into plural by user inputing the number

#The dictionary for number
numDict = {1:'one', 2:'two', 3:'three', 4:'four',
           5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine', 10:'ten'}
exception = {'person':'people', 'mouse':'mice', 'focus': 'foci','deer':'deer', 'potato':'potatoes', 'man':'men', 'child':'children'}

#there are some exceptions the english when converting
#user input
numInt = int(input('Please Enter the number of the object(1~10): '))
#check for invalid input of number
for i in range(1,10):
    if numInt < 1 or numInt > 10:
        print('This input is Invalid')
        numInt = int(input('Please Enter the number again(1~10): '))

#then ask the user for the object
object = input('Please Enter an object: ')

#checking for the number whether it should be converted or not
if numInt > 1 and numInt < 10:
    if object[-1:] == 'a' or object[-1:] == 'i' or object[-1:] == 'o' or object[-1:] == 'u' \
            or object[-1:] == 'x' or object[-1:] == 'z' or object[-1:] == 's' \
            or object[-2:] == 'ch' or object[-2:] == 'sh':
        p = object + 'es'

    elif object[-1:] == 'y':
        if object[-2:] == 'a' or object[-2:] == 'e' or \
            object[-2:] == 'i' or object[-2:] == 'o' or object[-2:] == 'u':
            p = object + 's'
        else:
            p = object.replace('y', 'ies')
    elif object in exception.keys():
            p = exception[object]
    else:
        p = object + 's'
    print(numDict[numInt] + ' ' + p)
else:
    p = object
    print(numDict[numInt] + ' ' + p)
