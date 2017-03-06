import time
import signal

TIMEOUT = 10
TIMEOUT2 = 0
p = 0
ptime = 0
LS = 20
LB = 30
AS = 30
AB = 50
ES = 25
EB = 40
while True:
    #Ordering coffee
    print('This are the three types of coffee: ')
    print('1 - Latte')
    print('2 - Americano')
    print('3 - Expresso')
    c = int(input('What type of coffee would you like to order?(Type in the number): '))

    if c >= 4:
        print('Invalid input.')
        print(' ')
        continue

    print('This are the sizes for coffee: ')
    print('1 - BIG')
    print('2 - SMALL')
    size = int(input('What size of coffee would you like?(Type in the number): '))

    if size >= 3:
        print('Invalid input.')
        continue

    TandP = [[6, LB, LS], [4, AB, AS], [5, EB, ES]]

    Tuple = TandP[c-1]
    ptime = Tuple[0]
    if size == 1:
        p = Tuple[1]
        print(p)
    elif size == 2:
        p = Tuple[2]
        print(p)
    else:
        print('Please order again.')


    s = int(input('How many sugar would you like?(0-5): '))
    ps = s*1
    t = p + ps
    print('The total price is: ' + str(t))

    print('Would you like to start or cancel?(START/CANCEL): ')

    signal.alarm(TIMEOUT)
    sin = input()
    signal.alarm(0) # disable the alarm after success

    if sin == 'START':
        print('The time required for preparation is: ' + str(ptime) + ' s.')
        boom = ptime
        while boom > 0:
            time.sleep(1)
            print(boom)
            boom -=1
        if boom == 0:
            print('READY')
            break

    else:
        continue
