import myLib as ml
import random

def randomWord(words, density):
    '''
    The function generates the word amount the user enters
    :param density: listing next possible words
    :param words: list of probability that calcualte the words
    :return: the random words generate from the list
    '''
    n = random.random()
    index = 0
    while n > density[index]:
        index += 1
    return words[index]


userword = input('Please enter the first word: ')
usernum = int(input('How many words you want to generate? '))

sampletext = 'Lyrics'
text = ml.readText(sampletext)

predicte = ''

#generate the amount of words
for i in range(usernum):

    nextWord, freq = ml.findNextWord(userword, sampletext)
    probList = ml.probOcurrence(freq)
    prob = ml.probOcurrence(probList)
    word = randomWord(nextWord, prob)
    predicte += (' ' + word)

print(predicte)
'''
ml.findNextWord('the', text)
'''
