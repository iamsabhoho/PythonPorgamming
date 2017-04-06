#The purpose of this program is to add up all the value the user input and count the iteration.

vinput = 1
vAcc = 0
iter = 0

while True:
    vinput= input('Please enter your value(0 - 100). Any character to exit: ')
    #print(type(vinput))
    try:
        v = int(vinput)
        if isinstance(v, int) == True:
            if 0 <= v <= 100:
                vAcc += v
                iter +=1
                print(vAcc/iter)
                print(str(vAcc) + (' ') + str(iter))
                continue
            else:
                continue

        print('Final: ' + str(vAcc) + (' ') + str(iter))

    except ValueError:
        #Handle the exception
        print(vAcc/iter)
        print('It is not an integer.')
        break







