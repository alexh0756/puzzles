def snakesAndLadders(board):
    """
    this solves the game if the player is forced to keep
    taking ladders and snakes until there is none one the
    current spot
    """
    
    n = len(board)
    last_tile = n**2 - 1
    starts = [0]
    moves = [0]
    move = 0

    for start, cur_move in zip(starts, moves):
        move = cur_move + 1

        check = []
        val = []
        for i in range(1, 7):
            loc = start + i
            if loc > last_tile:
                break
            row = n - (loc // n) - 1
            col = abs((loc) % n - ((n - 1) * ((n - row - 1) % 2)))
            if board[row][col]==-1:
                val.append(loc)
            else:
                check.append(board[row][col]-1)

        if val:
            check.append(val[-1])
            # if (i == 6) or (loc == last_tile) or (board[row][col] > 0):
        for loc in check:
            path = [-2]
            row = n - (loc // n) - 1
            col = abs((loc) % n - ((n - 1) * ((n - row - 1) % 2)))
            while ((board[row][col] - 1) > 0) and (board[row][col] - 1) not in path:
                loc = board[row][col] - 1
                path.append(loc)
                row = n - (loc // n) - 1
                col = abs((loc) % n - ((n - 1) * ((n - row - 1) % 2)))

            if loc in starts:
                continue
            starts.append(loc)
            moves.append(move)
        
        if last_tile in starts:
            break

    move = -1
    if last_tile in starts:
        idx = starts.index(last_tile)
        move = moves[idx]

    return move


def snakesAndLadders(board):
    
    n = len(board)
    last_tile = n**2 - 1
    starts = [0]
    moves = [0]
    move = 0

    for start, cur_move in zip(starts, moves):
        move = cur_move + 1

        check = []
        val = []
        for i in range(1, 7):
            loc = start + i
            if loc > last_tile:
                break
            row = n - (loc // n) - 1
            col = abs((loc) % n - ((n - 1) * ((n - row - 1) % 2)))
            if board[row][col]==-1:
                val.append(loc)
            else:
                check.append(board[row][col]-1)
        if val:
            check.append(val[-1])
        for loc in check:
            if loc in starts:
                continue
            starts.append(loc)
            moves.append(move)
        
        if last_tile in starts:
            break

    move = -1
    if last_tile in starts:
        idx = starts.index(last_tile)
        move = moves[idx]

    return move


board = [
    [-1,-1,30,14,15,-1],
    [23,9,-1,-1,-1,9],
    [12,5,7,24,-1,30],
    [10,-1,-1,-1,25,17],
    [32,-1,28,-1,-1,32],
    [-1,-1,23,-1,13,19]
]
snakesAndLadders(board)


board = [
    [-1,15,9,1,-1],
    [-1,-1,10,5,19],
    [18,-1,23,9,-1],
    [1,13,-1,16,20],
    [-1,10,10,25,13]
]
snakesAndLadders(board)


board = [
    [-1,10,-1,15,-1],
    [-1,-1,18,2,20],
    [-1,-1,12,-1,-1],
    [2,4,11,18,8],
    [-1,-1,-1,-1,-1]
]
snakesAndLadders(board)

board = [
    [1,1,-1],
    [1,1,1],
    [-1,1,1]
]
snakesAndLadders(board)


# board = [
#     [-1,-1],
#     [-1,3]
# ]
# snakesAndLadders(board)


board = [
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,35,-1,-1,13,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,15,-1,-1,-1,-1]
]
snakesAndLadders(board)