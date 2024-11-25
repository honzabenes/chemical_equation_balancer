
import re

# patterns for input parsing
PATTERN_SPLIT_MOLECULES = r'(?=[A-Z][a-z]*\d*)'
PATTERN_SPLIT_ELEMENTS = r'(?=\d)'

# returns the list, which contains molecules of one of the sides in the given equation
# example: ['Na', 'Cl2']
def getSideOfEquation(side: str, equation: str):
    if side == 'left':
        index = 0
    elif side == 'right':
        index = 1
    return [word.strip() for word in equation.split('=')[index].split('+')]

# returns the list, which contains molecules of one of the sides in the given equation, but each molecule is represented by another list, which contains elements of this molecule and their count
# example: [['Na'], ['Cl2']]
def formatSideOfEquation(side: list):
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
def createMatrixOfChemEquation(equation: list, elements: list):
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
    def pivot(problematicMatrix, indexOfDiagonalZero: int):
        i = indexOfDiagonalZero + 1
        while (i < len(problematicMatrix)) and (problematicMatrix[i][indexOfDiagonalZero] == 0):
            i += 1
        if i == len(problematicMatrix):
            return False
        else:
            pivottedMatrix = problematicMatrix
            pivottedMatrix[indexOfDiagonalZero], pivottedMatrix[i] = pivottedMatrix[i], pivottedMatrix[indexOfDiagonalZero]
            return pivottedMatrix

    # BODY of the gauss funciton
    for row in range(len(matrix)):

        # reason for "row < len(matrix) - 1": when solving chemical equation, one zero-line always appears, the "pivot" function makes it the last row of the matrix
        if (matrix[row][row] == 0) and (row < len(matrix) - 1):
            matrix = pivot(matrix, row)
            if not matrix:
                return False
            
        for j in range(row + 1, len(matrix)):
            factor = - matrix[j][row] / matrix[row][row]
            for column in range(row, len(matrix[0])):
                matrix[j][column] += matrix[row][column] * factor
    
    while len(matrix) >= len(matrix[0]):
        matrix.pop()
    return matrix
    
# returns the roots of the system of equations (stoichiometric coefficients) in the list
def backSubst(upperTriangularMatrix):

    WIDTH = len(upperTriangularMatrix[0])
    HEIGHT = len(upperTriangularMatrix)
    roots = [0] * WIDTH
    roots[WIDTH - 1] = 1
    for i in range(HEIGHT - 1, -1, -1):
        sum = 0

        for j in range(WIDTH - 1, i, -1):
            sum += upperTriangularMatrix[i][j] * roots[j]
            
        roots[i] = -sum / upperTriangularMatrix[i][i]

    # expanding roots to be whole numbers if they are not yet
    for i in range(len(roots)):
        counter = 1
        root = roots[i]
        while roots[i] % 1 != 0:
            roots[i] += root
            counter += 1
        if counter > 1:
            for k in range(len(roots)):
                if k != i:
                    roots[k] *= counter
        
        roots[i] = int(roots[i])

    return roots


# ===== MAIN PROGRAM =====

output_lines = []

with open('input/file.txt') as file:
    for line in file:

        left_side = formatSideOfEquation(getSideOfEquation('left', line))
        right_side = formatSideOfEquation(getSideOfEquation('right', line))

        equation = left_side + right_side
        elements = getElementsOfEquation(equation)
        matrix_of_equation = createMatrixOfChemEquation(equation, elements)

        gaussMatrix = gauss(matrix_of_equation)
        roots = backSubst(gaussMatrix)

        output_line = ''
        for i in range(len(equation)):
            if roots[i] > 1:
                molecule = str(roots[i])
            else:
                molecule = ''
            for j in range(len(equation[i])):
                molecule += equation[i][j]

            output_line += molecule
            if (i != len(left_side) - 1) and (i < len(equation) - 1):
                output_line += ' + '
            elif i < len(equation) - 1:
                output_line += ' = '

        output_line += '\n'

        output_lines.append(output_line)

# ===== OUTPUT =====
with open('output/file.txt', 'w') as file:
    file.writelines(output_lines)
    

