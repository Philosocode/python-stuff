theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
			'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
			'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
	print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
	print('-+-+-')
	print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
	print('-+-+-')
	print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X' # Set the default turn to 'X'
for i in range(9): # Load the board
	printBoard(theBoard) # Print the Board
	print('Turn for ' + turn + '. Move on which space?') # Indicate turn.
	move = input() # Move = user's input.
	theBoard[move] = turn # DICT 'theBoard' @ 'move' = 'X' or 'Y'
	if turn == 'X': # If turn is 'X' , reverse it.
		turn = 'O'
	else:
		turn = 'X'
