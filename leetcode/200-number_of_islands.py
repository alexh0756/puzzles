def number_of_islands(grid):

    n, m = len(grid), len(grid[0])
    coord = []
    for i in range(n):
        for j in range(m):
            coord.append((i, j))

    island_num = 0
    map_islands = {}
    while len(coord) > 0:
        i, j = coord[0]
        if grid[i][j] == 0:
            coord.pop(0)
            continue
        if island_num not in map_islands:
            map_islands.update({island_num: [coord[0]]})
            check_points = [coord[0]]
            while check_points:
                new_points = []
                for i, j in check_points:
                    for a in [-1, 0, 1]:
                        for b in [-1, 0, 1]:
                            if (a==b==0) or (not -1<i+a<n) or (not -1<j+b<m):
                                continue
                            if (grid[i+a][j+b]=='0') or ((i+a, j+b) in map_islands[island_num]):
                                continue
                            new_points.append((i+a, j+b))
                            map_islands[island_num].append((i+a, j+b))
                            grid[i+a][j+b] = '0'
                check_points = new_points

        i += 1

    return len(map_islands)

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