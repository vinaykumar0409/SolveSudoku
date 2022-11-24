def isSafe(board, row, col, target):
    i = 0
    while i < 9:
        if board[i][col] == target:
            return False
        i += 1
    i = 0
    while i < 9:
        if board[row][i] == target:
            return False
        i += 1
    rowBox = (row//3) * 3
    colBox = (col // 3) * 3
    for i in range(rowBox, rowBox + 3):
        for j in range(colBox, colBox + 3):
            if board[i][j] == target:
                return False
    return True
    
def solveSudoku(board):
    #Implement Your Code Here
    row = -1
    col = -1
    for i in range(9):
        flag = 0
        for j in range(9):
            if board[i][j] == 0:
                row = i
                col = j
                flag = 1
                break
        if flag:
            break
    if row == -1:
        for i in board:
            print(*i,sep=' ',end = ' ')
            print()
        return True
    for i in range(1, 10):
        if isSafe(board, row, col, i):
            board[row][col] = i
            if solveSudoku(board):
                # print(board)
                return True
            board[row][col] = 0
        
    return False

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
solveSudoku(board)
