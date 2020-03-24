#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

#open file and witer the contents

#          file name,  mode 
f = open('test.txt', 'w') # file description, file handler, w:write r:read
f.write("\n")
f.write("I am coding the test file\n")
f.write('''
Pls read the following lines:
1. Without you, the world is so lonely.
2. Distance makes the two hearts closer.
3. Encourage me when I need a drive.
Cool Cool Cool Cool This This  
''')
f.close()
#test  

#read all info in file
s = f.read() #size is the parameter
print('open for read...')
print(s)
f.close()

#read info by line
f = open('test.txt', 'r')
countLine = 0
while True:
    s = f.readline() # read one line
    if s == "":
        break
    print('count Line:', countLine)
    print(s)
    countLine += 1
f.close()

#read info by lines

f = open('test.txt', 'r')
s = f.readlines()  # read lines : more, not just one line
print('open for read...')
print(s)  # list, []  [1,2,6,]

for str in s: # List Iter
    print(str)
    print("---------------")
f.close()

# try to find the count of the word that appears
#read info by lines
allWords = []
f = open('test.txt', 'r')
s = f.readlines() #list 
for str in s: #element of List
    allWordsInStr = str.split() #list  split()
    for word in allWordsInStr:
        allWords.append(word)
f.close()
print (allWords)

wordDict = {}  # define dict with NULL 
# key: value(count)
wordDict["name"] = "Luke"
wordDict["Age"] = 9


for everyWord in allWords:
    if everyWord in wordDict: #if this work is in dict
        wordDict[everyWord] += 1
    else:
        wordDict[everyWord] = 1

print(wordDict)

items = wordDict.items()  # get [key:value]  [word:count]
print(items)

tmpitems=[] # temp var
for v in items:
    tmpitems.append([[v[1],v[0]]]) #reverse
print("tmpitems:",tmpitems) 

tmpitems.sovrt(reerse=True)
print("lst sort:")
print(tmpitems)

