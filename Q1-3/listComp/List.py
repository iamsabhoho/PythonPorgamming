#printing out list in different ways

'''list1 = [1,3,5,7,9]
list2 = [2,4,6,8,10]
merge = []

for i in range(len(list1)):
    merge.append(list1[i])
    if i < len(list2):
        merge.append(list2[i])
print(merge)


squares = []
for x in range(11):
    if x % 2 != 0:
        squares.append(x**2)

print(squares)

squares = [x**2 for x in range(11) if x % 2 != 0]

print(squares)'''

'''A = [1,2,3]
B = [1,5,6]
C = []

for a in A:
    for b in B:
        if a != b:
            C.append((a,b))
print(C)

C = [(a,b) for a in A for b in B if a != b]
print(C)'''

#Count the occurence of 'the'
text = 'the quick brown fox jumps over the lazy dog'
convert = text.split()
a = 0
x = [1 for i in convert if i == 'the']
print(sum(x))
'''for i in range(len(convert)):
    if convert[i] == 'the':
        a += 1
print(a)'''


'''
#One line python code
a = [x**2 for x in range(1,11) if x % 2 == 0]
print(a)
'''
