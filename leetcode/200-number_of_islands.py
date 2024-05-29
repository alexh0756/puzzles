def number_of_islands(grid):

    n, m = len(grid[0]), len(grid)
    map_islands = {}

    for x in range(n):
        for y in range(m):
            if grid[y][x] == '0':
                continue
            map_islands[(x,y)] = []
            if x > 0 and grid[y][x-1] == '1':
                map_islands[(x, y)].append((x-1,y))
            if y > 0 and grid[y-1][x] == '1':
                map_islands[(x, y)].append((x,y-1))
            if x < n - 1 and grid[y][x+1] == '1':
                map_islands[(x, y)].append((x+1,y))
            if y < m - 1 and grid[y+1][x] == '1':
                map_islands[(x, y)].append((x,y+1))

    islands = 0
    stack = []
    while map_islands:
        stack = [list(map_islands.keys())[0]]
        i = 0
        while i < len(stack):
            for each in map_islands[stack[i]]:
                if each not in stack:
                    stack.append(each)
            map_islands.pop(stack[i])
            i += 1
        islands += 1


    return islands



def numIslands(grid) -> int:
    num = 0
    def dfs(i: int, j: int):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return
        # now this cell is 1, after visited, mark it as 0
        grid[i][j] = '0'
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i , j - 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                num += 1
                dfs(i, j)

    return num


grid = [
  ["1","0","1","0","1"],
  ["1","0","1","0","1"],
  ["1","0","1","0","1"],
  ["1","1","1","0","1"]
]
print(numIslands(grid))


grid = [
  ["1","0","1","0","1"],
  ["1","0","1","0","1"],
  ["1","0","1","0","1"],
  ["1","1","1","0","1"]
]
print(number_of_islands(grid))


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(number_of_islands(grid))

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(number_of_islands(grid))