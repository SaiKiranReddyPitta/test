
def tic_tac_toe(game):   
    winner = []
    for row in game:
        if row[0] == row[1] == row[2]:
           winner.append(row[0])
    for i in range(0,3):
        if game[0][i] == game[1][i] == game[2][i]:
           winner.append(game[0][i])
    if game[0][0] == game[1][1] == game[2][2]:
           winner.append(game[0][0])
    if game[2][0] == game[1][1] == game[0][2]:
       winner.append(game[0][2])
    if len(winner) == 0:
       print('draw')
       return None
    if len(winner) == 1:
        if winner[0] == 'x' or winner[0] == 'o':
           print(winner[0])
        else:
           print("invalid input")
        return winner[0]
    else:
       print("invalid game")
       return None
def main():
    game = []
    for _ in range(0, 3):
       col_1 = input().split(' ')
       game.append(col_1)
    tic_tac_toe(game)
    if __name__ == '__main__':
    main()
    def tic_tac_toe(game):
    winner = []
    for row in game:
        if row[0] == row[1] == row[2]:
           winner.append(row[0])
    for i in range(0,3):
        if game[0][i] == game[1][i] == game[2][i]:
           winner.append(game[0][i])
    if game[0][0] == game[1][1] == game[2][2]:
           winner.append(game[0][0])
    if game[2][0] == game[1][1] == game[0][2]:
       winner.append(game[0][2])
    if len(winner) == 0:
       print('draw')
       return None
    if len(winner) == 1:
        if winner[0] == 'x' or winner[0] == 'o':
           print(winner[0])
        else:
           print("invalid input")
        return winner[0]
    else:
        print("invalid game")
        return None
def main():
    game = []
    for _ in range(0, 3):
       col_1 = input().split(' ')
       game.append(col_1)
    tic_tac_toe(game)
if __name__ == '__main__':
    main()

