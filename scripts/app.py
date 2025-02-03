
import sys
import parse_chem_equation as pce
import gaussian_elimination as ge

def calcStoichCoeff(outputFile: str):
    '''Read chemical equations from the input file and write enumerated equations with stoichiometric coefficients into the output file.'''
    output_lines = []

    # line = sys.stdin.read()
    for line in sys.stdin:

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

        if ut_matrix == False:
            output_line = 'Error: cannot calculate this chemical equation'
            output_line += '\n'
            output_lines.append(output_line)
            continue
        
        roots = ge.backSubst(ut_matrix)   # roots are the stoichometric coefficients

        if roots == False:
            output_line = 'Error: cannot calculate this chemical equation'
            output_line += '\n'
            output_lines.append(output_line)
            continue

        if len(output_line) == 0:
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
        output_lines.append(output_line)


    with open(outputFile, 'w') as file:
        file.writelines(output_lines)
