import urllib.request #Python module for retrueving url pages

#url with the vocabulary
req = urllib.request.Request('https://archive.org/stream/TheChroniclesOfNarnia/The%20Chronicles%20of%20Narnia_djvu.txt')
#open the url
response = urllib. request.urlopen(req)
#read the html file: decode using utf-8
the_page = response.read().decode("utf-8")

glossary = the_page.split()

for w in glossary:
    if '<pre' in w:
        start = glossary.index(w)
        print(start)
    if '</pre' in w:
        finish = glossary.index(w)
        print(finish)

narnia = glossary[start:finish]

lc = [w.lower() for w in narnia]

def printMenu(items, lwidth, rwidth, title):
    """
    Prints keys and values in a menu format
    :param items: dictionary
    :param lwidth: int
    :param rwidth: int
    :param title: string
    :return: items
    """
    t = title

    print(t.center(lwidth+rwidth, "-"))

    for k, v in items.items():
        print(k.ljust(lwidth, ".") + str(v).rjust(rwidth, "."))

    return items


#check each word and characters for punctuations
pun = ":;,.!?-"
for word in lc:
    for ch in word:
        if ch in pun:
            word.replace(ch, '')

newlist = lc.append(narnia)

#bubble sort
def bubbleSort(items):
    """
    bubble sorting
    :param items:
    :param index:
    :return:
    """
    index = list(range(len(items)))

    for i in range(items):
        for j in range(len(items)-i-1):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[i]
    print(items)
    return items, index

def prebuble(wordbanklist):
    """
    this function sorted the bank of words
    :param wordbanklist: list of unsorted tuples
    :return: list of tuples so then it can go to bubble sort later on
    """
    items = [element[1] for element in wordbanklist]
    items_sort, index = bubbleSort(items)
    sortwordbank = [wordbanklist[i] for i in index]

    return sortwordbank

#insertion sort
def insertionSort(items):
    """
    insertion sorting
    second method to sort the occurence of the words
    :param items:
    :return:
    """
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
    print(items)
    return items

i = {}
for j in lc[1:100]:
    if 'x' not in i.keys():
        i[j] = lc.count(j)


wordbank = {}

wblist = [(k,v) for k, v in wordbank.items()]

printMenu(i, 25, 15, "Words")
#print(bubbleSort([6,9,4,1]))
print(insertionSort(newlist))
