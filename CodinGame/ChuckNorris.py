message = input()
mList = []

#convert
for i in message:
    mList.append('{0:07b}'.format(ord(i))) #7-bit

#count the same char
count = 0

#find next one
for j in ''.join(mList):
    if j != None:
        print(('0' * count) + (' ' if count else "") + ('00 ' if j == '0' else '0'))
        count = 1
    else:
        count += 1

print('0'*count)
