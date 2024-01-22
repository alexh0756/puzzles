def rotate_image(matrix):

    n = len(matrix)

    if n == 1:
        return
    if n == 2:
        matrix[0][0], matrix[0][1], matrix[1][1], matrix[1][0] = matrix[1][0], matrix[0][0], matrix[0][1], matrix[1][1]

    for k in range(n-2):
        for i in range(1+k, n-k):
            matrix[k][i-1], matrix[i-1][-1-k], matrix[-1-k][-1*i], matrix[-1*i][k] = matrix[-1*i][k], matrix[k][i-1], matrix[i-1][-1-k], matrix[-1-k][-1*i]
            # matrix[k][i-1+k], matrix[i-1+k][-1-k], matrix[-1-k][-1*i-k], matrix[-1*i-k][k] = matrix[-1*i-k][k], matrix[k][i-1+k], matrix[i-1+k][-1-k], matrix[-1-k][-1*i-k]


    return matrix

print(rotate_image([[1,2],[3,4]]))
print(rotate_image([[val for val in range(10)] for va in range(10)]))
print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))
print(rotate_image([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))