import sys

board = None
game_won = False
RED_CHIP = "R"
YELLOW_CHIP = "Y"

def setup_board():
	global board 
	board = [[0 for i in range(7)] for j in range(6)]

def print_board():
	global board
	for row in board:
		print(row)

def game_loop():
	global game_won
	while game_won==False:
		red_column = input("Enter Column(0-6) for RED move: ")
		process_move(int(red_column), RED_CHIP)

		yellow_column = input("Enter Column(0-6) for Yellow move: ")
		process_move(int(yellow_column), YELLOW_CHIP)

def process_move(column, player_colour):
	#check valid list index
	#check column for existing chips
	#add chip

	#Check column num is within valid range - to avoid use of -1
	if(column>=0 and column<len(board[0])):

		try:
			for i in range(len(board)):
				#check if top row of column is full
				if (i==0 and board[i][column] != 0):
					print("Column is full")
					break

				#check bottom row
				elif (i==len(board)-1 and board[i][column]==0):
					board[i][column] = player_colour
					check_gamewon(i, column, player_colour)
					break

				#check rows between top (inclusive) and bottom
				elif board[i][column]!=0:
					board[i-1][column] = player_colour
					check_gamewon(i-1, column, player_colour)
					break

			print_board()

		except IndexError:
			print("Invalid move")
			print_board()
			return

	else:
		print("Invalid move: invalid column number, please enter a number between 0 and 6")

def check_gamewon(row_num, column_num, player_colour):
	won = False
	if (check_horizontal(row_num, player_colour)):
		won = True
	elif (check_vertical(column_num, player_colour)):
		won = True

	# check diagnol

	if(won):
		print_board()
		print("WIN WIN WIN WIN: congrats %s player!" % player_colour)
		sys.exit(0)
	else:
		print("Next move...")

def check_vertical(column_num, player_colour):
	winning_str = player_colour*4
	column_str = ''

	for i in range(len(board)):
		column_str += str(board[i][column_num])

	return winning_str in column_str

def check_horizontal(row_num, player_colour):
	winning_str = player_colour*4
	return winning_str in ''.join(str(x) for x in board[row_num])

def check_diagonal():
	pass

if __name__ == '__main__':
	setup_board()
	print_board()
	game_loop()

