# This will print a DICT in a similar format to picnicTable.py
def printInventory(itemDict, leftWidth, rightWidth):
	print('INVENTORY'.center(leftWidth + rightWidth, '-'))
	for k, v in itemDict.items():
		print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))


inventory = {'sword': 2, 'axe': 1, 'apples': 5, 'bazooka': 0, 'gold': 2000}
print("Enter left width.")
leftWidth = int(input("> "))
print("Enter right width.")
rightWidth = int(input("> "))

printInventory(inventory, leftWidth, rightWidth)