def readText(filepath):
    """
    read and return a text in a file
    :param filepath:
    :return:
    """
    f = open(filepath, 'r')
    returnText = f.read()
    f.close()
    return returnText.split()

def findNextWord(word, text):
    """
    find the words that appears in the text file
    :param word: the keywords
    :param text: the text file
    :return: a list of nextwords
    """
    nextWord, frequency = [], []
    for idx, wrd in enumerate(text):
        if wrd == word:
            #finding the next word
            nextWrd = text[idx+1]
            if nextWrd in nextWord:
                #counting the f
                frequency[nextWord.index(nextWrd)]+=1
            else:
                #if not yet on the list, add the word to the list,
                #f starts at 1
                nextWord.append(nextWrd)
                frequency.append(1)
    print(nextWord)
    print(frequency)
        #print('next word is {}'.format(text[idx+1]))
    return nextWord, frequency

def probOcurrence(count):
    nEvents = sum(count)
    prob = [1.0*x/nEvents for x in count]
    density = []
    total = 0
    for p in prob:
        total += p
        density.append(total)
    return density
'''
def randomWord(words, density):

    generate the next word
    :param words:
    :param density:
    :return:
   import random as rn
    n = rn.random()
    idx = 0
    while n > density[idx]:
        idx += 1
    return words[idx]

'''

def randomCmate(inputlist = ['Sabrina','Cici','Stephanie','Daniel','Darren']):
    '''
    select a classmate name at random
    return classmate name
    '''
    import random as rn

    NumStu = len(inputlist) - 1
    x = rn.randint(0, NumStu)

    name = inputlist[x]
    print(name)

    return name

def capitalize(words = ['Bob', 'JOHN','alice','bob','ALICE','J','Bob']):

    name = [x[0].upper() + x[1:].lower() for x in words if len(x) > 2]
    print(name)

    return name

def combinelists(colors = ['red','yellow','blue'], clothes = ['hat','shirt', 'pants']):
    x = [a + ' ' + b for a in colors for b in clothes]
    print(x)

    return x

def takeOutVowels(sentence = 'Your mother was a hamster', vowels = ['aeiou']):
    x = [l for l in sentence if l not in 'aeiou']
    print(x)

    s = ''
    for l in x:
        s+= l
    print(s)
    return s
