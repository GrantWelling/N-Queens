
#Create a n x n list of lists filled with 0's
def createBoard(n):
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)
    return board

#Print the board
def printBoard(board):
    for row in board:
        print(row)

def isComplete(board):
    #Check if there are n queens on the board and no two queens are attacking each other
    n = len(board)
    queens = 0
    #Keep track of the position we are checking throughout the loop
    
    for row in board:
        for square in row:
            if square == 1:
                queens += 1
                if not isSafe(board, (board.index(row), row.index(square))):
                    return False
                
    if queens == n:
        return True
    else:
        return False

    
    
def placeQueens(row):
    if 1 in row:
        for square in range(len(row)):
            if row[square] == 1:
                if square == len(row)-1:
                    row[square] = 0
                    return 'removed'
                else:
                    row[square] = 0
                    row[square+1] = 1
                    return square + 1
    else:
        row[0] = 1
        return 0
       
def isSafe(board, position):
    #Check if the position on the board is safe

    #Check the column
    for i in range(len(board)):
        if board[i][position[1]] == 1:
            if i != position[0]:
                return False
    
    #Check the diagonals
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                if (abs(i - position[0]) == abs(j - position[1])) and (i, j) != position:
                    return False
    return True
    
 
def queensGambit(board):
    n = len(board)
    row = 1
    board[0][0] = 1
    steps = 0
    while not isComplete(board):
        steps += 1
        queenPlaced = placeQueens(board[row])
        if queenPlaced == 'removed':
            row -= 1
            continue
        if isSafe(board, (row, queenPlaced)):
            row += 1
    print('It took', steps, 'steps to solve the problem for n =', n)
    return board
  
#Test the functions
board = createBoard(8)

print('Solution for n = 8')
nqueens = queensGambit(board)

printBoard(nqueens)

board = createBoard(4)
print('Solution for n = 4')
nqueens = queensGambit(board)
printBoard(nqueens)

board = createBoard(5)
print('Solution for n = 5')
nqueens = queensGambit(board)
printBoard(nqueens)

board = createBoard(30)
print('Solution for n = 30')
nqueens = queensGambit(board)
printBoard(nqueens)
