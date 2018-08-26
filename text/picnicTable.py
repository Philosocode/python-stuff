# FUNC that takes DICT and two Widths as ARGs.
def printPicnic(itemsDict, leftWidth, rightWidth):
	# STR 'PICNIC ITEMS' is printed in the center, surrounded by -
	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
	# Loop through Keys and Values in DICT.
	for k, v in itemsDict.items():
		# Key is printed on the left, followed by dots. VAL (integers) converted to Str; displayed on right.
		print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

# Define the Dict.
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 9001}
# Call FUNC.
printPicnic(picnicItems, 12, 5)
printPicnic(picnicItems, 20, 6)
