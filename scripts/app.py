
import re

# patterns used for parsing the input
PATTERN_SPLIT_MOLECULES = r'(?=[A-Z][a-z]*\d*)'
PATTERN_SPLIT_ELEMENTS = r'(?=\d)'

def getSideOfEquation(side: str, equation: str) -> list:
    '''Return list of strings, which contains all molecules from one side of the equation.
    
    example:

    left side, NaCl + H2SO4 = NaHSO4 + HCl -> ['NaCl', 'H2SO4']
    '''
    if side == 'left':
        index = 0
    elif side == 'right':
        index = 1
    return [molecule.strip() for molecule in equation.split('=')[index].split('+')]


def formatSideOfEquation(side: list) -> list:
    '''Format the given list containing all molecules from a side of the chemical equation represented as strings, so the molecules are represented as a string inside a list.
    
    example:

    ['NaCl', 'H2SO4'] -> [['Na', 'Cl'], ['H2', 'S', 'O4']]
    '''
    formattedSide = []
    for item in side:
        molecule = [element for element in re.split(PATTERN_SPLIT_MOLECULES, item) if element]
        formattedSide.append(molecule)
    return formattedSide

def getElementsOfEquation(equation: list) -> list:
    '''Return list containing elements, which appears in the equation.

    example:

    [['Na', 'Cl'], ['H2', 'S', 'O4'], ['Na', 'H', 'S', 'O4'], ['H', 'Cl']] -> ['Na', 'H', 'C', 'O', 'Cl']
    '''
    elements = []
    for molecule in equation:
        for element in molecule:
            element = re.split(PATTERN_SPLIT_ELEMENTS, element)[0]
            if element not in elements:
                elements.append(element)
    return elements

# explanation of how this function works: a(KNO3) = b(KNO2) + c(O2)
# K: 1a = 1b + 0c         K: 1a - 1b - 0c = 0        [1 -1  0]
# N: 1a = 1b + 0c   ==>   N: 1a - 1b - 0c = 0  ==>   [1 -1  0]
# O: 3a = 2b + 2c         O: 3a - 2b - 2c = 0        [3 -2 -2]
def createMatrixOfChemEquation(left_side: list, right_side: list, elements: list) -> list:
    '''Return matrix (list of lists) representing the chemical equation.'''
    equation = left_side + right_side

    lowerCaseAlphabet = []
    for i in range(97, 123):
        lowerCaseAlphabet.append(i)

    matrix = []

    for element in elements:
        row = []
        
        for i in range(len(equation)):
            count = 0

            for item in equation[i]:
                if item[:len(element)] == element:
                    if item[len(element):]:
                        # this if make sure, that the element is really the same as the item, for example Cl starts with C, but its not the same...
                        if ord(item[len(element)]) not in lowerCaseAlphabet:
                            count += int(item[len(element):])
                    else:
                        count += 1

                    if i >= len(left_side):
                        count = -count
                    
            row.append(count)

        matrix.append(row)

    return matrix

def gauss(matrix) -> list:
    '''Modify the matrix and return upper triangular matrix using Gaussian elimination.'''
    
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

    # BODY of the gauss funciton
    # function iterates over the rows only for "matrix width - 1" because there is always one parameter (stoichiometric coefficient) in the roots of each matrix that represents a chemical equation, so such a system of equations can always be modified to a system of n equations with n + 1 variables.
    for row in range(len(matrix[0]) - 1):

        if (matrix[row][row] == 0):
            matrix = pivot(matrix, row)
            if not matrix:
                return False
            
        for j in range(row + 1, len(matrix)):
            factor = - matrix[j][row] / matrix[row][row]
            for column in range(row, len(matrix[0])):
                matrix[j][column] += matrix[row][column] * factor
    
    # remove zero-lines
    while len(matrix) >= len(matrix[0]):
        matrix.pop()
    return matrix
    
# UTMatrix stands for "Upper Triangular Matrix"
def backSubst(UTMatrix) -> list:
    '''Return roots of the system of equations.'''

    WIDTH = len(UTMatrix[0])
    HEIGHT = len(UTMatrix)
    roots = [0] * WIDTH
    roots[WIDTH - 1] = 1
    for i in range(HEIGHT - 1, -1, -1):

        # calculating roots
        sum = 0
        for j in range(WIDTH - 1, i, -1):
            sum += UTMatrix[i][j] * roots[j]
        roots[i] = -sum / UTMatrix[i][i]
    
        # expanding roots to be whole numbers if they are not yet
        factor = 1
        root = roots[i]
        while roots[i] % 1 != 0:
            roots[i] += root
            factor += 1
        if factor > 1:
            for j in range(i + 1, len(roots)):
                roots[j] *= factor
        roots[i] = int(roots[i])

    return roots
