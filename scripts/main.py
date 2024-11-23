
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
def getElementsOfEquation(equation) -> list:
    elements = []
    for molecule in equation:
        for element in molecule:
            element = re.split(PATTERN_SPLIT_ELEMENTS, element)[0]
            if element not in elements:
                elements.append(element)
    return elements

# this function returns a matrix of chemical equation
# example: a(KNO3) = b(KNO2) + c(O2)
# K: 1a = 1b + 0c         K: 1a - 1b - 0c = 0        (1 -1  0)
# N: 1a = 1b + 0c   ==>   N: 1a - 1b - 0c = 0  ==>   (1 -1  0)
# O: 3a = 2b + 2c         O: 3a - 2b - 2c = 0        (3 -2 -2)
def createMatrixOfChemEquation(equation: list, elements: list) -> list: # of lists (matrix)
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

    # def gauss(matrix):
        
    #     def pivot(matrix, indexOfProblemRow):




# ===== MAIN PROGRAM =====

with open('input/file.txt') as file:
    for line in file:

        left_side = formatSideOfEquation(getSideOfEquation('left', line))
        right_side = formatSideOfEquation(getSideOfEquation('right', line))

        equation = left_side + right_side
        elements = getElementsOfEquation(equation)
        matrix_of_equation = createMatrixOfChemEquation(equation, elements)
    

        ### control prints ###
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

