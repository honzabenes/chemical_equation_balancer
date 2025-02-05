
import sys
import re
import parse_chem_equation as pce
import gaussian_elimination as ge

EQUATION_SYNTAX_PATTERN = r'^(?=(.*=.*$))(?=(.*\+.*$))(?=(.*[A-Z].*$))(?=(.*\s.*$))(?!(.*[a-z]{2,}.*$))(?!(\d+[a-zA-Z]))^[A-Za-z0-9()+=\s]+$'
# ^ – Začátek řetězce
# (?=(.*=.*$)) – Právě jedno =
# (?=(.*\+.*$)) – Alespoň jedno +
# (?=(.*[A-Z].*$)) – Alespoň jedno velké písmeno
# (?=(.*\s.*$)) – Alespoň jedna mezera
# (?!(.*[a-z]{2,}.*$)) – Nesmí obsahovat dvě malá písmena za sebou
# (?!(\d+[a-zA-Z])) – Čísla nesmí být na začátku slova
# ^[A-Za-z0-9()+=\s]+$ – Povolené znaky


def writeSyntaxError():
    output_line = 'Error: syntax error on this line'
    output_line += '\n'
    return output_line


def writeCalcError():
    output_line = 'Error: cannot calculate this chemical equation'
    output_line += '\n'
    return output_line


def calcStoichCoeff(line: str) -> str:
    '''Get the chemical equation and return the balanced chemical equation.'''
    if bool(re.fullmatch(EQUATION_SYNTAX_PATTERN, line)) == False:
        return writeSyntaxError()

    output_line = ''

    left_side = (pce.getSideOfEquation(True, line))
    right_side = (pce.getSideOfEquation(False, line))
    equation = left_side + right_side
        
    frmt_left_side = pce.formatSideOfEquation(left_side)
    frmt_right_side = pce.formatSideOfEquation(right_side)
    frmt_equation = frmt_left_side + frmt_right_side
    
    elements = pce.getElementsOfEquation(frmt_equation)
    matrix_of_equation = pce.createMatrixOfChemEquation(frmt_left_side, frmt_right_side, elements)

    ut_matrix = ge.gauss(matrix_of_equation)
    if not ut_matrix:
        return writeCalcError()
    
    roots = ge.backSubst(ut_matrix)   # roots are the stoichometric coefficients

    integer_roots = ge.balanceCoefficients(roots)

    for i in range(len(frmt_equation)):
        molecule = ''
        
        if integer_roots[i] > 1:   # add stoichometric coefficient if its bigger than 1
            molecule = str(integer_roots[i])

        molecule += equation[i]   # add the rest of the molecule
        output_line += molecule

        if i < len(equation) - 1:

            if (i != len(left_side) - 1):
                output_line += ' + '

            else:
                output_line += ' = '

    output_line += '\n'
    return output_line


def getOuput(outputFile: str):
    '''Write the output to the file.'''

    with open(outputFile, 'w') as file:
        for line in sys.stdin:
            file.write(calcStoichCoeff(line))
