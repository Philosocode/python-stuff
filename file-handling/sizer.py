'''
#! usr/bin/env python3
sizer.py - This file walks through a directory tree,
finds all files with size > 100MB,
and returns the absolute path of the file.
'''

import os


def get_file_size(file):
    file_size = os.path.getsize(file) / 1048576
    return round(file_size, 2)


current_dir = os.getcwd()

# Walk through a folder
for dirpath, dirnames, filenames in os.walk(current_dir):
    # Find files with size > 100MB (104857600 bytes)
    for file in filenames:
        abs_file = os.path.join(dirpath, file)
        file_size = get_file_size(abs_file)
        if file_size > 100:
            file = file.encode()
            # Print abs path
            print(f"Size of {file} is {file_size} MB")
