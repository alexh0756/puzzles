def setZeros(matrix):

    n, m = len(matrix), len(matrix[0])
    lst_i, lst_j = [], []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] != 0:
                continue

            if i not in lst_i:
                lst_i.append(i)
            if j not in lst_j:
                lst_j.append(j)

    for i in lst_i:
        for j in range(m):
            matrix[i][j] = 0
    
    for j in lst_j:
        for i in range(n):
            if i in lst_i:
                continue
            else:
                matrix[i][j] = 0

    return
print(setZeros([[i for i in range (-2, 200)] for j in range(200)]))
print(setZeros([[1,0,1]]))
print(setZeros([[1],[0],[1]]))
print(setZeros([[1,1,1],[1,0,1],[1,1,1]]))
print(setZeros([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))