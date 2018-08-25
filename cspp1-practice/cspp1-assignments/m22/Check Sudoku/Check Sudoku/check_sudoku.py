'''
    Sudoku is a logic-based, combinatorial number-placement puzzle.
    The objective is to fill a 9×9 grid with digits so that
    each column, each row, and each of the nine 3×3 subgrids that compose the grid
    contains all of the digits from 1 to 9.

    Complete the check_sudoku function to check if the given grid
    satisfies all the sudoku rules given in the statement above.
'''

def check_sudoku(sudoku):
    '''
        Your solution goes here. You may add other helper functions as needed.
        The function has to return True for a valid sudoku grid and false otherwise
    '''
def isValid(num,x,y):
    for i in range(9):
        if board[i][y]==num:
            return False
        if board[x][i]==num:
            return False
    row=x-x%3
    col=y-y%3
    for i in range(3):
        for j in range(3):
            if board[i+row][j+col]==num:
                return False
    return True
 
def solve(remaining):
    if remaining==0:
        return True
    for i in range(9):
        for j in range(9):
            if board[i][j]!=0:
                continue
            for num in range(1,10):
                if isValid(num,i,j):
                    board[i][j]=num
                    if solve(remaining-1):
                        return True
                    board[i][j]=0
            return False
    return False
 
def pp():
    for i in range(9):
        for j in range(9):
            print(board[i][j],end="")
        print()
    print()
 
board=[]
remaining=0
for i in range(9):
    a=list(map(int,list(input())))
    for j in a:
        if j==0:
            remaining+=1
    board.append(a)
    
def main():
    '''
        main function to read input sudoku from console
        call check_sudoku function and print the result to console
    '''
    
    # initialize empty list
    sudoku = []
    line = "123456789"
    # loop to read 9 lines of input from console
    for i in range(9):
        # read a line, split it on SPACE and append row to list
        row = input().split(' ')
        sudoku.append(row)
    # call solution function and print result to console
    print(check_sudoku(sudoku))

if __name__ == '__main__':
    main()