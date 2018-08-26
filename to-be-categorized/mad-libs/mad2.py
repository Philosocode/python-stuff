'''
#! usr/bin/env python3
mad2.py - A re-factored version that only uses one Regex
'''
import re


def replacer(madReg, madList, i, mo):
    newStr = ""

    if mo == "NOUN":
        newStr = madReg.sub(input("Enter a noun:\n"), madList[i])
    elif mo == "ADVERB":
        newStr = madReg.sub(input("Enter an adverb:\n"), madList[i])
    elif mo == "VERB":
        newStr = madReg.sub(input("Enter a verb:\n"), madList[i])
    elif mo == "ADJECTIVE":
        newStr = madReg.sub(input("Enter an adjective:\n"), madList[i])

    return newStr


def main():

    # STEP 1: READ TEXT FILE
    file_handle = open('mad.txt', 'r')
    madList = file_handle.readlines()

    # STEP 2: REGEX: noun, verb, adjective, adverb
    madReg = re.compile(r'noun|adverb|verb|adjective', re.I)

    # STEP 3: SCAN & REPLACE MATCHES
    for i in range(len(madList)):
        while madReg.search(madList[i]):
            mo = madReg.search(madList[i])
            madList[i] = replacer(madReg, madList, i, mo)

    print(madList)
    # STEP 3: WRITE TO NEW FILE
    # newMad = open('newMad.txt', 'w')
    # newMad.writelines(madList)

    # file_handle.close()
    # newMad.close()


main()
