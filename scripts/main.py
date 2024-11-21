
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

        matrix = []
        for element in elements:
            row = []

            for i in range(len(left_side)):
                isInMolecule = False
                for item in equation[i]:

                    if item[len(element):]:
                        count = int(item[len(element):])
                    else:
                        count = 1
                    item = item[:len(element)]

                    if element == item:
                        row.append(count)
                        print(element, 'is in', equation[i])
                        isInMolecule = True
                        
                if not isInMolecule:
                    count = 0
                    row.append(count)
                    print(element, 'is not in', equation[i])


            for i in range(len(left_side), len(left_side) + len(right_side)):
                isInMolecule = False
                for item in equation[i]:

                    if item[len(element):]:
                        count = int(item[len(element):])
                    else:
                        count = 1
                    item = item[:len(element)]

                    if element == item:
                        row.append(-count)
                        print(element, 'is in', equation[i])
                        isInMolecule = True
                        
                if not isInMolecule:
                    count = 0
                    row.append(count)
                    print(element, 'is not in', equation[i])

            matrix.append(row)


    
        print()
        
        print('LS formatted:', left_side)
        print('RS formatted:', right_side)

        print()

        print('Equation:', equation)

        print()

        print('Elements:', elements)

        print()

        print(matrix)

        print()

