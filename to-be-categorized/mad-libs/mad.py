'''
#! usr/bin/env python3
mad.py - Play madlibs
'''
import re

# STEP 1: READ TEXT FILE
file_handle = open('mad.txt', 'r')
madList = file_handle.readlines()

# STEP 2: SCAN: noun, verb, adjective, adverb
nounReg = re.compile('NOUN', re.I)
verbReg = re.compile('VERB', re.I)
adjReg = re.compile('ADJECTIVE', re.I)
advReg = re.compile('ADVERB', re.I)

for i in range(len(madList)):
    while nounReg.search(madList[i]) or verbReg.search(madList[i]) or adjReg.search(madList[i]) or advReg.search(madList[i]):
        if nounReg.search(madList[i]):
            newNoun = input("Enter a noun:\n")
            madList[i] = nounReg.sub(newNoun, madList[i])

        if advReg.search(madList[i]):
            newAdv = input("Enter an adverb:\n")
            madList[i] = advReg.sub(newAdv, madList[i])

        if verbReg.search(madList[i]):
            newVerb = input("Enter a verb:\n")
            madList[i] = verbReg.sub(newVerb, madList[i])

        if adjReg.search(madList[i]):
            newAdj = input("Enter an adjective:\n")
            madList[i] = adjReg.sub(newAdj, madList[i])

# STEP 3: WRITE TO NEW FILE
newMad = open('newMad.txt', 'w')
newMad.writelines(madList)

file_handle.close()
newMad.close()
