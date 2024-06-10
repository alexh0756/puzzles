def minimumTotal(triangle):

    array = [[None]*len(depth) for depth in triangle]
    array[0][0] = triangle[0][0]

    for i, level in enumerate(triangle[1:]):
        for j, num in enumerate(level):
            left, right = j-1, j
            if left < 0:
                left = right
            if right == len(array[i]):
                right = left
            array[i+1][j] = min(array[i][left], array[i][right]) + num
        
    return min(array[-1])

print(minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
