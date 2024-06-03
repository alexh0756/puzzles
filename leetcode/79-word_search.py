def exist(board, word):

    def backtrack(board, word, start):
        board[start[0]][start[1]] = '*'
        
        if not word:
            return True

        res = False
        for loc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            
            x = start[1] + loc[1]
            y = start[0] + loc[0]
            if not (0 <= y < len(board)):
                continue
            if not (0 <= x < len(board[0])):
                continue
            if word[0] != board[y][x]:
                continue
            res = backtrack(board, word[1:], (y, x))
            if res:
                return res

        return res

    starts = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                starts.append((i, j))

    
    for start in starts:
        res = backtrack([row[:] for row in board], word[1:], start)
        if res:
            return res

    return False

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"
print(exist(board, word))

board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "SEE"
print(exist(board, word))


board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCB"
print(exist(board, word))
