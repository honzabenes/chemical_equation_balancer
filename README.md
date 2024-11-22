# Chemical Equation Balancer

## Overview

This program is designed to balance chemical equations by calculating the stoichiometric coefficients required to ensure the conservation of mass and atoms on both sides of the reaction. The input is a standard chemical equation, and the output includes formatted equations, a list of involved elements, and a matrix representation used for solving the equation.

---

## Features

- **Input Parsing**: Splits the chemical equation into molecules and individual elements for analysis.
- **Matrix Generation**: Constructs a coefficient matrix based on the presence and quantities of each element in the molecules.
- **Equation Analysis**:
  - Identifies unique elements present in the reaction.
  - Separates molecules into reactants and products.
- **Extensibility**: Code is structured to allow for additional functionality, like solving the matrix using Gaussian elimination.

---

## How It Works

1. **Input**:
   - A chemical equation (e.g., `KNO3 = KNO2 + O2`) is read from a file (`input/file.txt`).

2. **Processing**:
   - The equation is split into reactants and products using the function `getSideOfEquation`.
   - Molecules are broken down into individual elements and their counts using `formatSideOfEquation`.
   - A matrix is generated representing the conservation of each element using `createMatrixOfChemEquation`.

3. **Output**:
   - Lists of formatted reactants and products.
   - A matrix representation of the equation for further computations.

---

## Example

**Input**:  
`KNO3 = KNO2 + O2`

**Output**:
- Formatted Reactants: `[['K', 'N', 'O3']]`
- Formatted Products: `[['K', 'N', 'O2'], ['O2']]`
- Elements: `['K', 'N', 'O']`
- Matrix: `[[1, -1, 0], [1, -1, 0], [3, -2, -2]]`

---

## File Structure

- **`main.py`**: Contains the main program logic.
- **`input/file.txt`**: Input file with unbalanced chemical equations (one per line).

---

## Future Development

- **Matrix Solving**: Implement Gaussian elimination or other numerical methods to solve for stoichiometric coefficients.
- **GUI Integration**: Build a user interface for easier input and visualization of balanced equations.
- **Error Handling**: Add input validation for incorrectly formatted chemical equations.

---

## Usage

1. Place your chemical equations in `input/file.txt`, one equation per line.
2. Run the program:
3. View the outputs in the console.

---

## Requirements

- Python 3.7 or higher
- Required libraries: `re`

---

## Contributing

Feel free to fork the repository and submit pull requests with enhancements or bug fixes.

## Author

Jan Beneš

## License

This project is licensed under the MIT License.
