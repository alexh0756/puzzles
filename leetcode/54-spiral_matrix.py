def spiralOrder(matrix):

    if len(matrix) == 1:
        return matrix[0]
    if len(matrix[0]) == 1:
        return [val[0] for val in matrix]

    lst = []
    n = len(matrix) * len(matrix[0])

    dims = [len(matrix), len(matrix[0])]
    idx = [0, 0]
    pointer = 1
    direction = [1, 1]
    counter, passes = 0, 0

    while len(lst) < n:
        if counter >= dims[pointer] - 1:
            pointer = (pointer + 1) % 2
            if sum(direction) == 0:
                direction = [direction[1]] * 2
            else:
                direction[1] *= -1
            counter = 0
            passes += 1
            if passes > 2:
                dims[pointer] -= 1

        lst.append(matrix[idx[0]][idx[1]])
        idx[pointer] += 1 * direction[0]
        counter += 1

    return lst

# print(spiralOrder(matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]))
# print(spiralOrder(matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]))
# print(spiralOrder(matrix = [[0], [1], [2], [3], [4]]))
print(spiralOrder(matrix = [[0, 1, 2, 3, 4, 5,], [0, 1, 2, 3, 4, 5,], [0, 1, 2, 3, 4, 5,], [0, 1, 2, 3, 4, 5,], [0, 1, 2, 3, 4, 5,]]))
print(spiralOrder(matrix = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]]))
print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))
print(spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))