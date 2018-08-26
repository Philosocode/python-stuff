# IMPORTS
import os
import shutil

# Get extension
ends_with = input("What extension to search for? (include the .)\n> ")
print(ends_with)

# Get current folder
cur_folder = os.path.abspath(os.getcwd())
os.chdir(cur_folder)

# Create new folder
new_folder_name = input("Name of new folder?\n> ")
os.makedirs(new_folder_name)
# Get new folder path
new_folder = os.path.abspath(new_folder_name)

# Walk through current dir
for folder, subfolder, filename in os.walk(cur_folder):
    for file in filename:
        if file.endswith(ends_with):
            shutil.move(os.path.join(folder, file), new_folder)
