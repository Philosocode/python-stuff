tableData1 = [['apples', 'oranges', 'cherries', 'banana'],
         ['Alice', 'Bob', 'Carol', 'David'],
         ['dogs', 'cats', 'moose', 'goose']]

tableData2 = [['Agumon', 'Gabumon', 'Patamon', 'SuperDuperMon'],
			  ['A', 'AAA', 'AAAAA', 'AAAAAAAA'], 
			  ['Grim Reaper', 'Stuart', 'Hell\'s Angel is Coming to Town', 'Halp Me']]

'''
tableData[0] = Fruits	tableData[0][0] = apples	[0][1] = oranges	[0][2] = cherries	[0][3] = banana
tableData[1] = Names	tableData[1][0] = Alice		[1][1] = Bob		[1][2] = Carol		[1][3] = David
tableData[2] = Animals	tableData[2][0]	= dogs		[2][1] = cats		[2][2] = moose		[2][3] = goose
'''

def printTable(List):
	colWidths = [0] * len(List)	# tableData Length: 3
	innerList = len(List[0])		# innerList Length: 4

# Find the longest STR in each inner List and store the value in colWidths.
# e.g. longest STR in tableData[0] > colWidths[0]
	for i in range(innerList):	# 4; <0, 1, 2, 3>
		for e in range(len(List)):	# 3; <0, 1, 2>
			colWidths[e] = len(max(List[e], key=len))
			print(List[e][i].rjust(colWidths[e]), ' ', end='')
		print('')


# Print tableData in a Table.
# Each column: rjust(colWidth[i])
# Here's what it should look like: 

'''
  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose

00.rjust(colWidths[0])	10.rjust(colWidths[1]) 20.rjust(colWidths[2])
01.rjust(colWidths[0])	11.rjust(colWidths[1]) 21.rjust(colWidths[2])
02.rjust(colWidths[0])	12.rjust(colWidths[1]) 22.rjust(colWidths[2])
03.rjust(colWidths[0])	13.rjust(colWidths[1]) 23.rjust(colWidths[2])

LOOP #1: Add 1 to Digit #1. [0, 1, 2]
LOOP #2: Add 1 to Digit #2, based on Length of Inner List.
'''

while True:
	print("\nWhich table do you want to print?")
	print("Options: 1, 2, Q")

	response = input("> ")

	if response == '1':
		printTable(tableData1)
	elif response == '2':
		printTable(tableData2)
	elif response == 'Q':
		break
	else:
		print("Nope, try again.")