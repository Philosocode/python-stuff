catNames = []	# Create an empty List.

# Create a WHILE-Loop.
while True:
	print("Enter the name of cat " + str(len(catNames) + 1) +	# Cat number determined by the len of List
		" (Or enter nothing to stop):")
	name = input()	# Get the user's input.
	if name == '':	# If input is empty, break out of the Loop.
		break
	catNames = catNames + [name] # List Concatenation

print("The cat names are: ")
for name in catNames:	# For each name stored in List 'catNames':
	print(name)			# Print the name.