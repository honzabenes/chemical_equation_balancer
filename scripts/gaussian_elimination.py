
from fractions import Fraction

def pivot(matrix, indexOfDiagonalZero: int) -> list:
    '''Try to swap rows of the matrix if a zero appears on the main diagonal, if not possible, return False.'''
    i = indexOfDiagonalZero + 1
    while (i < len(matrix)) and (matrix[i][indexOfDiagonalZero] == 0):
        i += 1

    if i == len(matrix):
        return False
    
    else:
        matrix[indexOfDiagonalZero], matrix[i] = matrix[i], matrix[indexOfDiagonalZero]
        return matrix


def gauss(matrix) -> list:
    '''Modify the matrix and return upper triangular matrix using Gaussian elimination.'''
    
    unknownsCount = len(matrix[0])
    equationsCount = len(matrix)
    parametersCount = unknownsCount - equationsCount

    if parametersCount > 1:   # gaussian elimination cannot resolve chemical equation when there is more than 1 parameter
        return False

    for row in range(unknownsCount - 1):

        if  (matrix[row][row] == 0):
            pivottedMatrix = pivot(matrix, row)

            if pivottedMatrix:  # function "pivot" found row to swap
                matrix = pivottedMatrix
            else:   # function "pivot" found no row to swap
                return False
            
        for j in range(row + 1, equationsCount):
            factor = - matrix[j][row] / matrix[row][row]
            for column in range(row, unknownsCount):
                matrix[j][column] += matrix[row][column] * factor
    
    while equationsCount >= unknownsCount:   # remove zero lines
        matrix.pop()
        equationsCount -= 1

    return matrix
    

# UTMatrix stands for "Upper Triangular Matrix"
def backSubst(UTMatrix) -> list:
    '''Return roots of the system of equations.'''
    WIDTH = len(UTMatrix[0])
    HEIGHT = len(UTMatrix)

    roots = [0] * WIDTH

    roots[WIDTH - 1] = 1
        
    for i in range(HEIGHT - 1, -1, -1):
        sum = 0
        for j in range(WIDTH - 1, i, -1):
            sum += UTMatrix[i][j] * roots[j]
        roots[i] = -sum / UTMatrix[i][i]

    return roots


def gcd(a, b):
    '''Find the greatest common denominator of numbers a and b.'''
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a

    return a


def lcm(a, b):
    '''Find the least common multiple of numbers a and b.'''
    return abs(a * b) // gcd(a, b)


def lcmMultiple(numbers):
    '''Find the least common multiple of multiple numbers.'''
    result = lcm(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        result = lcm(result, numbers[i])

    return result
    

def balanceCoefficients(coefficients: list) -> list:
    """Balance the chemical coefficients so that they are whole."""

    fractions = [Fraction(c).limit_denominator() for c in coefficients]

    denominators = [frac.denominator for frac in fractions]

    commonDenominator = lcmMultiple(denominators)

    integerCoefficients = [int(frac * commonDenominator) for frac in fractions]

    return integerCoefficients
