# Import the os module.
import os

# Set the total size.
totalSize = 0;
# Okay. os.listdir will list all the files in '/Users/Eremes/Desktop'
for filename in os.listdir('/Users/Eremes/Desktop'):
	totalSize = totalSize + 
	# Get the size (in bytes) of /Users/Eremes/Desktop/'filename', as found in os.listsdir()
	# NOTE: path.join is used to connect the folder name to the file name.
	os.path.getsize(os.path.join('/Users/Eremes/Desktop', filename))

print(totalSize)