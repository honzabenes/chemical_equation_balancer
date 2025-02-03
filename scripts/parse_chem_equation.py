
import re

# patterns used for parsing the input
PATTERN_REMOVE_SQUARE_BRACKETS = r'\[|\]'
PATTERN_SPLIT_PARENTHESES = r'\(.*?\)\d*'
PATTERN_EXTRACT_FUNC_GROUP = r'\((.*?)\)'
PATTERN_SPLIT_MOLECULES = r'(?=[A-Z][a-z]*\d*)'
PATTERN_SPLIT_ELEMENTS = r'(?=\d)'

def getSideOfEquation(side: bool, equation: str) -> list:
    '''Return list of strings, which contains all molecules in the wanted side of the equation.

    "Side" argument:
    True if you want the function to return parsed left side, False if right.
    
    Example:

    getSideOfEquation(True, NaCl + H2SO4 = NaHSO4 + HCl) -> ['NaCl', 'H2SO4']
    '''
    if side == True:
        index = 0
    elif side == False:
        index = 1

    return [molecule.strip() for molecule in equation.split('=')[index].split('+')]


def formatSideOfEquation(side: list) -> list:
    '''Format the given list containing all molecules of the chemical equation side represented as strings, so each molecule is represented as a list of the single elements.
    
    Example:

    formatSideOfEquation(['NaCl', 'H2SO4']) -> [['Na', 'Cl'], ['H2', 'S', 'O4']]
    '''
    formattedSide = []

    for molecule in range(len(side)):
        side[molecule] = re.sub(PATTERN_REMOVE_SQUARE_BRACKETS, '', side[molecule])

    for item in side:

        if '(' in item:
            funcGroup = re.search(PATTERN_SPLIT_PARENTHESES, item).group()   # get the whole function group
            rBrcktIndex = funcGroup.index(')')
            funcGroupCount = int(funcGroup[rBrcktIndex + 1 :])   # get the count of the function group
            funcGroup = re.search(PATTERN_EXTRACT_FUNC_GROUP, funcGroup).group(1)   # get the function group without parentheses and count

            expandedGroup = ''
            for element in re.findall(r'[A-Z][a-z]?\d*', funcGroup):   # divide the function group into elements with their counts
                elementSymbol = re.match(r'[A-Z][a-z]?', element).group()
                elementCount = int(re.search(r'\d+', element).group()) if re.search(r'\d+', element) else 1   # get the count of the element if there is any, otherwise set it to 1
                expandedGroup += elementSymbol + str(elementCount * funcGroupCount)
            
            item = item.replace(f'({funcGroup}){funcGroupCount}', expandedGroup)

        formattedSide.append(re.findall(r'[A-Z][a-z]?\d*', item))

    return formattedSide


def getElementsOfEquation(equation: list) -> list:
    '''Return list containing all elements that appears in the equation.

    Example:

    getElementsOfEquation([['Na', 'Cl'], ['H2', 'S', 'O4'], ['Na', 'H', 'S', 'O4'], ['H', 'Cl']]) -> ['Na', 'H', 'C', 'O', 'Cl']
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
                        if ord(item[len(element)]) not in lowerCaseAlphabet: # make sure, that the element is exactly the same as the item, for example Cl starts with C, but its not the same
                            count += int(item[len(element):])
                    else:
                        count += 1

                    if i >= len(left_side):
                        count = -count
                    
            row.append(count)

        matrix.append(row)

    return matrix
