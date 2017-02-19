def addM(a, b):
    res = []
    for i in range(len(a)):
        row = []
        for j in range(len(a[0])):
            row.append(a[i][j]+b[i][j])
        res.append(row)
    return res


matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]
rmatrix = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]
for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
                rmatrix[i][j] = matrix1[i][j] + matrix2[i][j]


for r in rmatrix:
        print(r)
