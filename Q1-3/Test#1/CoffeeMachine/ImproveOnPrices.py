ptime = 0
LS = 20
LB = 30
AS = 30
AB = 50
ES = 25
EB = 40

c = int(input())
size = int(input())
'''
if c == 1:
    ptime = 6
    if size == 1:
        p = LB
    else:
        p = LS

elif c == 2:
    ptime = 4
    if size == 1:
        p = AB
    else:
        p = AS

elif c == 3:
    ptime = 5
    if size == 1:
        p = EB
    else:
        p = ES
else:
    print('Please order again.')
'''

TandP = [[6, LB, LS], [4, AB, AS], [5, EB, ES]]

Tuple = TandP[c-1]
ptime = Tuple[0]
if size == 1:
    p = Tuple[1]
    print(p)
else:
    p = Tuple[2]
    print(p)













'''

if size == 1:
    if c == 1:
        p = LB
    elif c == 2:
        p = AB
    else:
        p = EB
elif size == 2:
    if c == 1:
        p = LS
    elif c == 2:
        p = AS
    else:
        p = ES
else:
    print('Please order again.')

if c == 1:
    ptime = 6
elif c == 2:
    ptime = 4
else:
    ptime = 5


if c == 1 and size == 1:
    p = LB
elif c == 1 and size == 2:
    p = LS
elif c == 2 and size == 1:
    p = AB
elif c == 2 and size == 2:
    p = AS
elif c == 3 and size == 1:
    p = EB
elif c == 3 and size == 2:
    p = ES
else:
    print('Please order again.')

if c == 1:
    ptime = 6
elif c == 2:
    ptime = 4
else:
    ptime = 5
'''
