import random

def gameOfLife(board):

    n, m = len(board), len(board[0])
    storage = {}

    for i in range(n):
        for j in range(m):
            counter = 0
            for a in range(-1, 2):
                for b in range(-1, 2):
                    if a == b == 0 or 0 > i + a or i + a > n - 1 or 0 > j + b or j + b > m - 1:
                        continue
                    if board[i+a][j+b] == 1:
                        counter += 1
            if counter < 2 and board[i][j] != 0:
                storage.update({(i, j): 0})
            elif counter > 3 and board[i][j] != 0:
                storage.update({(i, j): 0})
            elif counter == 3 and board[i][j] != 1:
                storage.update({(i, j): 1})

    for (i, j), val in storage.items():
        board[i][j] = val

    return board


def a(board):
    for i in board:
        print(i)
    print()

[[random.randint(0, 1) for i in range(25)] for j in range(25)]

a(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))