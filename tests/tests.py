
# run cmd: python -m unittest discover -s tests

import unittest
from scripts.parse_chem_equation import *
from scripts.gaussian_elimination import *

class TestParseChemEquation(unittest.TestCase):
    def test_getSideOfEquation(self):
        self.assertEqual(
            getSideOfEquation(True, 'S + O2 = SO2'), ['S', 'O2']
            ) # test left side of equation
        self.assertEqual(
            getSideOfEquation(False, 'S + O2 = SO2'), ['SO2']
            ) # test right side of equation
        self.assertEqual(
            getSideOfEquation(True, 'Fe2(SO4)3 + NaOH = Fe(OH)3 + Na2SO4'), ['Fe2(SO4)3', 'NaOH']
        ) # test left side of equation with parentheses

    def test_formatSideOfEquation(self):
        self.assertEqual(
            formatSideOfEquation(['S', 'O2']), [['S'], ['O2']]
            ) # test formatting side of equation
        self.assertEqual(
            formatSideOfEquation(['Fe2(SO4)3', 'NaOH']), [['Fe2', 'S3', 'O12'], ['Na', 'O', 'H']]
        ) # test formatting side of equation with parentheses

    def test_getElementsOfEquation(self):
        self.assertEqual(
            getElementsOfEquation([['S'], ['O2']]), ['S', 'O']
            )
        self.assertEqual(
            getElementsOfEquation([['Fe2', 'S3', 'O12'], ['Na', 'O', 'H']]), ['Fe', 'S', 'O', 'Na', 'H']
        )

    def createMatrixOfChemEquation(self):
        self.assertEqual(
            createMatrixOfChemEquation([['S'], ['O2']], [['SO2']], ['S', 'O']), [[1, 0, -1], [0, 2, -2]]
        )


class TestGaussElimination(unittest.TestCase): # my gaussian elimination is adjusted for the calculation of stoichiometric coefficients
    def test_gauss(self):
        self.assertEqual(
            gauss([[1, 0, -1], [0, 2, -3]]), [[1, 0, -1], [0.0, 2.0, -3.0]]
        ) # matrix is already in UT form

        self.assertEqual(
            gauss([[1, 0, -1, 0], [2, 1, -3, -1], [0, 1, -2, 0], [0, 1, 0, -2]]), [[1, 0, -1, 0], [0.0, 1.0, -1.0, -1.0], [0.0, 0.0, -1.0, 1.0]]
        ) # 4 parameters and 4 equations, create the UT matrix and remove one line (there is always 1 free parameter in chem equation)

        self.assertEqual(
            gauss([[2, 2, 0, 0, 0, -2, 0], [2, 4, 4, -4, -4, -1, -2], [0, 1, 0, -1, -1, 0, 0], [0, 0, 1, -2, 0, 0, 0], [0, 0, 1, 0, -1, 0, 0]]), False
        ) # 2 free parameters in UT matrix, so the chemical equation cannot be resolved this way


if __name__ == '__main__':
    unittest.main(verbosity=2)
