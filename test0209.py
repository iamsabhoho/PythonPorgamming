import myLib

ch = 'a'
while ord(ch) is not 27:
    ch = myLib.getkey()
    print(ch)

    if ch is 'w':
        print('')

