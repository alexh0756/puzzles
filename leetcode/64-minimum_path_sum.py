def minPathSum(grid):

    m, n = len(grid[0]), len(grid)

    paths = [[None]*m for i in range(n)]

    paths[0][0] = grid[0][0]
    i = 0
    while paths[n-1][m-1] == None:
        for j in range(i, m):
            if i == 0 and j == 0:
                continue
            if i == 0:
                min_path = paths[i][j-1]
            else:
                min_path = min(paths[i][j-1], paths[i-1][j])

            paths[i][j] = grid[i][j] + min_path
        
        
        for j in range(i+1, n):
            if i == 0:
                min_path = paths[j-1][i]
            else:
                min_path = min(paths[j][i-1], paths[j-1][i])

            paths[j][i] = grid[j][i] + min_path
        i += 1

    return paths[-1][-1]

print(minPathSum(grid = [[1,2],[5,6],[1,1]]))
print(minPathSum(grid = [[0]]))
print(minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))
print(minPathSum(grid = [[1,2,3],[4,5,6]]))
