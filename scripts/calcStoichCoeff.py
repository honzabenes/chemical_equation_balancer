
import app

def calcStoichCoeff(IFile, OFile): # 'input/file.txt', 'output/file.txt'
    output_lines = []

    # ===== INPUT =====
    with open(IFile) as file:
        for line in file:

            left_side = app.formatSideOfEquation(app.getSideOfEquation('left', line))
            right_side = app.formatSideOfEquation(app.getSideOfEquation('right', line))

            equation = left_side + right_side
            elements = app.getElementsOfEquation(equation)
            matrix_of_equation = app.createMatrixOfChemEquation(left_side, right_side, elements)

            ut_matrix = app.gauss(matrix_of_equation)
            roots = app.backSubst(ut_matrix)

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
    with open(OFile, 'w') as file:
        file.writelines(output_lines)
