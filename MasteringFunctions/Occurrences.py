#Write a function that counts how many times a word appears in a text.
#Use the function you wrote in #5.
#For example: text = “The house of the flying tigers and the flying roaches”
#number of occurrences of ‘the’ = 3, ‘house’ = 1, ‘flying’ = 2, etc

text = 'the house of the flying tigers and the flying roaches'
convert = text.split()
print(type(convert))

def appearence():
    for i in range(len(text)):
        word = convert.count(convert[i])
        print(str(convert[i]) + ' appears ' + str(word) + ' time(s).')

appearence()

