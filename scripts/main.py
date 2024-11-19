
import re

# patterns for input parsing
pattern_molecules = r'(?=[A-Z][a-z]*\d*)'
pattern_elements = r'(?=\d)'

# this function returns a list, which contains molecules of one of the sides in the given equation
def getSideOfEquation(side: str, equation: str):
    if side == 'left':
        index = 0
    elif side == 'right':
        index = 1
    else:
        print('wrong parameter.')
    return [word.strip() for word in equation.split('=')[index].split('+')]

# this function also returns a list, which contains molecules of one of the sides in the given equation, but each molecule is represented by another list, which contains elements of this molecule and their count
def formatSideOfEquation(side: list):
    formattedSide = []
    for item in side:
            molecule = [element for element in re.split(pattern_molecules, item) if element]
            formattedSide.append(molecule)
    return formattedSide


# ===== MAIN PROGRAM =====

with open('../input/file.txt') as file:
    for line in file:

        left_side = formatSideOfEquation(getSideOfEquation('left', line))
        right_side = formatSideOfEquation(getSideOfEquation('right', line))

        # creates list of all elements in equation
        elements = []
        equation = left_side + right_side
        for molecule in equation:
            for element in molecule:
                element = re.split(pattern_elements, element)[0]
                if element not in elements:
                    elements.append(element)

    
    print()
    
    print('LS formatted:', left_side)
    print('RS formatted:', right_side)

    print()

    print('Elements:', elements)

    print()

