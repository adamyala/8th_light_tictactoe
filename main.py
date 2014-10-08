board = [
	[1 , 2 , 3],
	[4 , 5 , 6],
	[7 , 8 , 9]
]

clear_board = [
	[1 , 2 , 3],
	[4 , 5 , 6],
	[7 , 8 , 9]
]

coor_to_spot = {
	"00" : 1,
	"01" : 2,
	"02" : 3,
	"10" : 4,
	"11" : 5,
	"12" : 6,
	"20" : 7,
	"21" : 8,
	"22" : 9
}
spot_to_coor = {
	1 : "00",
	2 : "01",
	3 : "02",
	4 : "10",
	5 : "11",
	6 : "12",
	7 : "20",
	8 : "21",
	9 : "22",
}

win_lines = [
	[1,2,3],
	[4,5,6],
	[7,8,9],
	[1,4,7],
	[2,5,8],
	[3,6,9],
	[1,5,9],
	[3,5,7]
]

def spot_to_board(spot):
	loc = list(spot_to_coor[int(spot)])
	return board[int(loc[0])][int(loc[1])]

def print_board(board):
	print ""
	for i in range(3):
		print " "+str(board[i][0])+" | "+str(board[i][1])+" | "+str(board[i][2])+" "
		if i != 2: print "___|___|___"
	print "   |   |   "
	print ""
	return

def user_first():
	print "Would you like to go first or second?"
	response = raw_input("Type 1 to go first or 2 to go second.\nOr type EXIT to quit: ")
	if response == "EXIT":
		return
	elif response == "1":
		start_game(True)
	elif response == "2":
		start_game(False)
	else:
		print ""
		print "I didn't understand that."
		user_first()

def spot_is_free(spot):
	if isinstance(spot_to_board(spot), int):
			return True
	else:
		return False

def take_user_move():
	spot = raw_input("Pick a spot to move: ")
	if isinstance(int(spot), int):
		if 0 < int(spot) <= 9:
			if spot_is_free(spot):
				return int(spot)
			else:
				print "Pick an unoccupied spot."
				take_user_move()
		else:
			print "Pick a spot of or between 1 and 9."
			take_user_move()
	else:
		print "I didn't understand that."
		take_user_move()

def winline_to_row(line):
	result = [] * 3
	result[0] = spot_to_board(line[0])
	result[1] = spot_to_board(line[1])
	result[2] = spot_to_board(line[2])
	return result

import random
def comp_move(user_first):
	for line in win_lines:
		row = winline_to_row(line)
		if row.count('X') == 2 and row.count('O') == 0:
			for 
	if not user_first:
		return 5
	else

	move = random.randint(1,9)
	while not spot_is_free(move):
		move = random.randint(1,9)
	return move

def update_board(spot, shape):
	loc = list(spot_to_coor[spot])
	loc[0] = int(loc[0])
	loc[1] = int(loc[1])
	board[loc[0]][loc[1]] = shape
	return

def winner():
	for line in win_lines:
		spot1 = spot_to_board(line[0])
		spot2 = spot_to_board(line[1])
		spot3 = spot_to_board(line[2])
		if spot1 == spot2 == spot3 == 'X':
			print "X wins!"
			return True
		if spot1 == spot2 == spot3 == 'O':
			print "O wins!"
			return True
	return False

def play_again():
	response = raw_input("Play again? Type yes or no. ")
	if response.lower() == "no":
		print "Thanks for playing!"
	elif response.lower() == "yes":
		user_first()
	else:
		print "I didn't understand that."
		play_again()

def clear_board():
	count = 1
	for i in range(3):
		for j in range(3):
			board[i][j] = count
			count += 1

def start_game(user_first):
	clear_board()
	print ""
	print "Lets play tic-tac-toe!"
	print "You're O's."
	if user_first:
		print_board(board)
		move = take_user_move()
		update_board(move, 'O')
	while winner() == False:
		update_board(comp_move(user_first), 'X')
		print_board(board)
		move = take_user_move()
		update_board(move, 'O')
	print_board(board)
	play_again()

user_first()