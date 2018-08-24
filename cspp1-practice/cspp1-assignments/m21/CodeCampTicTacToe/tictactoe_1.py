
def isvalidinput(board):
	x_sum = 0
	o_sum = 0
	
	sum = 0
	for i in board:
		x_sum += i.count('x')
		o_sum += i.count('o')  #remove and watch x_sum and o_sum 
	
		sum += i.count('o') + i.count('x') + i.count(".")
		if sum == 9:
			print("invalid input") 
			return
		if (x_sum - o_sum not in (0, 1, -1)):
			print("invalid game")
			return
		return True
		

def checkhorizontal(board):
	for i in range(len(board)):
		if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
			return board[i][0]

def checkvertical(board):
	for i in range(len(board)):
		if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
			return board[0][i]

def checkdiagonal(board):
	if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
		return board[0][0]
	if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
		return board[0][2]

def Checkwinner(board):
	winner = checkhorizontal(board)
	
	winner1 = checkvertical(board)
	
	winner2 = checkdiagonal(board)
	if (winner and winner1) or (winner1 and winner2) or (winner2 and winner):
		print("invalid game")

	if winner: #and winner in 'xo': #winner == x or #winner == o #for only either horizontal or vertical
		return winner
	if winner1:
		return winner
	if winner2:
		return winner
	else:
		return "draw"

def main():
    '''main function'''
    board = []
    for i in range (3):
    	board.append(input().split())
    if isvalidinput(board):
    	print("")
    #print(board)
    print(Checkwinner(board))

if __name__ == '__main__':
    main()