from itertools import permutations
import itertools
import requests

list_3 = []
#Permutauion
def permu(string):
    list_1 = []
    for idx in range(1, len(string)+1):
        list_1.append(list(''.join(p) for p in permutations(string, idx)))
    print(list_1)
    return list_1

#Web Scrappy
def getWords():
    url = "http://www.puzzlers.org/pub/wordlists/unixdict.txt"
    fetchData = requests.get(url)
    wordList = fetchData.content
    wordList = wordList.decode("utf-8").split()
    return wordList

#Compare two list and make 3rd list
def isOrdered():
    collection = getWords()
    for a in collection:
        for b in list_2:
            if a == b:
                list_3.append(b)

word = list(input("Enter Words: "))
list_2 = list(itertools.chain.from_iterable(permu(word)))
isOrdered()

def Sorting(lst):
    lst2 = sorted(lst, key=len)
    return lst2

for e in Sorting(list_3):
    print(e)
