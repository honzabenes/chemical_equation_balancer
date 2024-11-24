def gauss(matrix):
    
    # solves the problem when zero appears on the main diagonal and returns modified matrix if possible, if not, returns False
    def pivot(matrix, indexOfDiagonalZero):
        i = indexOfDiagonalZero + 1
        while (i < len(matrix)) and (matrix[i][indexOfDiagonalZero] == 0):
            i += 1
        if i == len(matrix):
            return False
        else:
            matrix[indexOfDiagonalZero], matrix[i] = matrix[i], matrix[indexOfDiagonalZero]
            return matrix

    # gauss BODY
    for row in range(len(matrix)):

        if (matrix[row][row] == 0) and (row < len(matrix) - 1):
            if pivot(matrix, row) == False:
                return False
            
        for j in range(row + 1, len(matrix)):
            factor = - matrix[j][row] / matrix[row][row]
            for column in range(row, len(matrix[0])):
                matrix[j][column] += int(matrix[row][column] * factor)
        
    return matrix

matrix1 = [[2,1,3],[4,3,7],[6,5,1]]
matrix2 = [[0,2,3],[1,4,5],[0,0,0]]
matrix3 = [[1,2,3],[2,4,6],[0,0,2]]

print(gauss(matrix1))
print(gauss(matrix2))
print(gauss(matrix3))