
import re

# patterns for input parsing
PATTERN_SPLIT_MOLECULES = r'(?=[A-Z][a-z]*\d*)'
PATTERN_SPLIT_ELEMENTS = r'(?=\d)'

# returns the list, which contains molecules of one of the sides in the given equation
# example: ['Na', 'Cl2']
def getSideOfEquation(side: str, equation: str) -> list:
    if side == 'left':
        index = 0
    elif side == 'right':
        index = 1
    return [word.strip() for word in equation.split('=')[index].split('+')]

# returns the list, which contains molecules of one of the sides in the given equation, but each molecule is represented by another list, which contains elements of this molecule and their count
# example: [['Na'], ['Cl2']]
def formatSideOfEquation(side: list) -> list:
    formattedSide = []
    for item in side:
            molecule = [element for element in re.split(PATTERN_SPLIT_MOLECULES, item) if element]
            formattedSide.append(molecule)
    return formattedSide

# returns the list of all elements which appears in the given equation
def getElementsOfEquation(equation: list) -> list:
    elements = []
    for molecule in equation:
        for element in molecule:
            element = re.split(PATTERN_SPLIT_ELEMENTS, element)[0]
            if element not in elements:
                elements.append(element)
    return elements

# returns a matrix of chemical equation
# example: a(KNO3) = b(KNO2) + c(O2)
# K: 1a = 1b + 0c         K: 1a - 1b - 0c = 0        (1 -1  0)
# N: 1a = 1b + 0c   ==>   N: 1a - 1b - 0c = 0  ==>   (1 -1  0)
# O: 3a = 2b + 2c         O: 3a - 2b - 2c = 0        (3 -2 -2)
def createMatrixOfChemEquation(equation: list, elements: list) -> list: # list of lists (matrix)
    matrix = []
    for element in elements:
        row = []
        
        for i in range(len(equation)):
            count = 0

            for item in equation[i]:
                if item.startswith(element):
                    if item[len(element):]:
                        count += int(item[len(element):])
                    else:
                        count += 1

                    if i >= len(left_side):
                        count = -count
                    
            row.append(count)

        matrix.append(row)

    return matrix

# modifies the given matrix and returns the upper triangular matrix using Gaussian elimination
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

    # BODY of the gauss funciton
    for row in range(len(matrix)):

        # reason for "row < len(matrix) - 1": when solving chemical equation, one zero-line always appears, the "pivot" function makes it the last row of the matrix
        if (matrix[row][row] == 0) and (row < len(matrix) - 1):
            if pivot(matrix, row) == False:
                return False
            
        for j in range(row + 1, len(matrix)):
            factor = - matrix[j][row] / matrix[row][row]
            for column in range(row, len(matrix[0])):
                matrix[j][column] += int(matrix[row][column] * factor)
        
    return matrix



# ===== MAIN PROGRAM =====

with open('input/file.txt') as file:
    for line in file:

        left_side = formatSideOfEquation(getSideOfEquation('left', line))
        right_side = formatSideOfEquation(getSideOfEquation('right', line))

        equation = left_side + right_side
        elements = getElementsOfEquation(equation)
        matrix_of_equation = createMatrixOfChemEquation(equation, elements)
    

        # ===== control prints =====
        print()
        print('LS formatted:', left_side)
        print('RS formatted:', right_side)

        print()

        print('Equation:', equation)

        print()

        print('Elements:', elements)

        print()

        print('Matrix:', matrix_of_equation)

        print()

        print('Matrix after Gauss:', gauss(matrix_of_equation))

        print()

