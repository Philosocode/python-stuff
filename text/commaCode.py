# Create an Empty List
myList = []

# FUNC: takes the User's List, splits it with commas, and adds 'and' to the end.
def listString(userList):
	partOne = userList[:-1]
	partTwo = userList[-1]
	print(', '.join(partOne) + ' and ' + partTwo + '.\n')

print("Type stuff to add to the List.\nType 'stop' to stop.")
# Create a WHILE-Loop and adds User Input to 'myList'.
while True:
	msg = input('> ')

	if msg == "stop": # If the user types 'stop', break and run FUNC 'listString'
		break
	else:
		myAdd = myList.append(msg)	# Add the user's input to 'myList'

print(myList)	# Print the List.

print("\nOkay, now we will separate the List.\n")
listString(myList)