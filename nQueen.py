def is_safe(board,row,col):
    
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    for i in range(row,-1,-1):
        j = col - (row-i)
        if j >=0 and board[i][j] == 1:
            return False

    for i in range(row,-1,-1):
        j = col + (row-i)
        if j <len(board) and board[i][j] == 1:
            return False
        
    return True
    



def solve_nQueen(board , row):
    n = len(board)

    if row == n :
        return True
    
    for col in range(n):
        if is_safe(board,row,col):
            board[row][col] = 1
            if solve_nQueen(board,row+1):
                return True
            board[row][col] =0 

    return False



def nqueen(n):
    board = [[0]*n for i in range(n)]

    if solve_nQueen(board,0):
        return board
    else:
        return None

    
def printMatrix(board):
    for i in board:
        for j in i:
            print(j,end=' ') 
        print()

n = 4 
result = nqueen(n)
if result:
    print('Postions found')
    printMatrix(result)
else:
    print('Not Found')
