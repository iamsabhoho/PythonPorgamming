#Write a function that combines two lists by alternatingly taking elements,
#e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
#Validate that the inputs have the same length before attempting to join them.

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
merge = []

for i in range(len(list1)):
    merge.append(list1[i])
    if i < len(list2):
        merge.append(list2[i])
print(merge)
