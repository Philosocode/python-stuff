'''
#! usr/bin/env python3
regSearch.py - Open all .txt files in folder & search for regex expression.
Print results to screen.
'''

import re
import os

# Get regex from user and store in 'userRegex'
userSearch = input("What regex to userSearch for?\n> ")
userRegex = re.compile(userSearch)

# Open all .txt files in current DIR
for file in os.listdir():
    if file.endswith(".txt"):
        with open(file) as file_handler:
            for line in file_handler:
                if userRegex.search(line):
                    print("\'{}\' found in {}:".format(userSearch, file_handler.name), end='')
                    print(" \"" + line + "\"")
                else:
                    print("\'{}\' not found in {}.".format(userSearch, file_handler.name))
