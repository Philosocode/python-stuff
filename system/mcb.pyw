#! /usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mxb.pyw save <keyword> - Saves clipboard to the keyword.
#        py.exe mcb.pyw <keyword> - Loads the keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
# Save keywords into shelf, load by opening shelf.

import shelve
import pyperclip
import sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
# There will be 3 'ARGs': 'save', the keyword, and the content
if len(sys.argv) == 3 and sys.argv[1].lower() == "save":
    # Keyword at index 2 (not 'save') = key, value = clipboard content
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':   # If the user types 'list'
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])


mcbShelf.close()
