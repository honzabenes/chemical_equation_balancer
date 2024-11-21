
import re

# patterns for input parsing
PATTERN_SPLIT_MOLECULES = r'(?=[A-Z][a-z]*\d*)'
PATTERN_SPLIT_ELEMENTS = r'(?=\d)'

# this function returns a list, which contains molecules of one of the sides in the given equation
def getSideOfEquation(side: str, equation: str):
    if side == 'left':
        index = 0
    elif side == 'right':
        index = 1
    return [word.strip() for word in equation.split('=')[index].split('+')]

# this function also returns a list, which contains molecules of one of the sides in the given equation, but each molecule is represented by another list, which contains elements of this molecule and their count
def formatSideOfEquation(side: list):
    formattedSide = []
    for item in side:
            molecule = [element for element in re.split(PATTERN_SPLIT_MOLECULES, item) if element]
            formattedSide.append(molecule)
    return formattedSide

# this function returns a matrix of chemical equation
# example: a(KNO3) = b(KNO2) + c(O2)
# K: 1a = 1b + 0c         K: 1a - 1b - 0c = 0        (1 -1  0)
# N: 1a = 1b + 0c   ==>   N: 1a - 1b - 0c = 0  ==>   (1 -1  0)
# O: 3a = 2b + 2c         O: 3a - 2b - 2c = 0        (3 -2 -2)
def createMatrixOfChemEquation():
    matrix = []
    for element in elements:
        row = []
        
        for i in range(len(equation)):
            isInMolecule = False

            for item in equation[i]:
                if item[len(element):]:
                    count = int(item[len(element):])
                else:
                    count = 1

                item = item[:len(element)]
                if element == item:
                    if i >= len(left_side):
                        count = -count
                    row.append(count)
                    isInMolecule = True
                    
            if not isInMolecule:
                row.append(0)

        matrix.append(row)
    return matrix


# ===== MAIN PROGRAM =====

with open('input/file.txt') as file:
    for line in file:

        left_side = formatSideOfEquation(getSideOfEquation('left', line))
        right_side = formatSideOfEquation(getSideOfEquation('right', line))

        # creates list of all elements which appears in the given equation
        elements = []
        equation = left_side + right_side
        for molecule in equation:
            for element in molecule:
                element = re.split(PATTERN_SPLIT_ELEMENTS, element)[0]
                if element not in elements:
                    elements.append(element)

        matrix_of_equation = createMatrixOfChemEquation()
    
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

