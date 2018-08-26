'''
#! usr/bin/env python3
renameDates.py - Renames filenames with American MM-DD-YYYY date format
to European DD-MM-YYYY.
'''

import shutil
import os
import re

# Create regex that matches American date format.
datePattern = re.compile(r"""
    ^(.*?)          # .*? matches anything; gets all the text before the date.
    ((0|1)?\d)-     # The Month: starts with 0 or 1. The ? means its optional.
    ((0|1|2|3)?\d)- # The Day: the first digit is optional ?
    ((19|20)\d\d)   # The Year: first 2 digits will be 19XX or 20XX |
    (.*?)$          # all text after the date $
    """, re.VERBOSE)

# Loop over files in working DIR.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip file names without a date.
    if mo == None:
        continue    # Move on to the next file.

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # Form European-style filename
    euroFilename = beforePart + dayPart + monthPart + yearPart + afterPart

    # Get absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # Rename files
    print("Renaming " % s" to " % s"...' % (amerFilename. euroFilename))
    # shutil.move(amerFilename, euroFilename) # uncomment after testing
