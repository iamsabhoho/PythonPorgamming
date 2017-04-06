#Given a non-negative integer number, repeatedly add all its digits
#until the result has only one digit. Draw the flow diagram and write a Python script.45

num = int(input('Please enter a non-negative integer: '))
#print(num)
while True:
    v = 0
    while num >= 0:
        if int(num/10) == 0:
            v += num%10
            #print("if: " + str(v) + ' ' + str(num))
            break
        else:
            v += num%10
            num = int(num/10)
            #print("else: " + str(v) + ' ' + str(num))

    if v >= 10:
        num = v
        #print("new num: " + str(num))
    else:
        print(str(v))
        break
