#Write the accumulated sum of a list.
#For example, if the input is [1, 2, 3, 4, 5],
#then the output should be [1, 3, 6, 10, 15].
p = 1
list = [1,2,3,4,5]
print(list[0])
for i in range(len(list)-1):
    p += list[i]+1
    print(p)

