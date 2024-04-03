# you can write to stdout for debugging purposes, e.g.
print("This is a debug message")
from random import randint

class Boardcell:
    def __init__(self):
        self.mine = False
        self.revealed = False
        self.count


def generateBoard(n, m):
    board = []
    for i in range(n):
        board[i] = []
        for j in range(n):
            board[i][j] = Boardcell()
    
    k = m
    while k > 0:
        r = randint(0, n)
        c = randint(0, n)
        if not board[r][c].mine:
            board[r][c].mine = True
            k -= 1
        
def performClickAction(x, y, board):
    n = len(board)
    if x > n-1 or x < 0:
        return 'x out of bound'
    if y > n-1 or y < 0:
        return 'y out of bound'

    if board[x][y].mine:
        return 'gameover'

    return traverse(x, y, n, board)

def traverse(x, y, n, board):
    if board[x][y].count > 0:
        return False
    
    count = 0
    for i in range(x-1, x+1):
        for j in range(y-1, y+1):
            if i-1 >= 0 and j-1 >= 0 and i+1 >= n-1 and j+1 >= n-1 and board[i][j].mine:
                count += 1

    board[x][y].count = count
    board[x][y].revealed = True
    if count > 0:
        return False

    for i in range(x-1, x+1):
        for j in range(y-1, y+1):
            if i-1 >= 0 and j-1 >= 0 and i+1 >= n-1 and j+1 >= n-1:
                traverse(i, j, n, board)


# M 2 M
# 1 2 1
#  -1 -1