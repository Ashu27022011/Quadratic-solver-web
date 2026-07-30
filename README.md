A small program
# Quadratic Solver Web

A simple and interactive web application built with **Python** and **Streamlit** that solves quadratic equations and visualizes their graphs.

## Features

* Solve quadratic equations of the form:

  [
  ax^2 + bx + c = 0
  ]

* Calculates:

  * Real or complex roots
  * Discriminant
  * Nature of roots
  * Vertex of the parabola
  * Axis of symmetry

* Interactive graph of the quadratic function

* Simple and beginner-friendly interface

## Technologies Used

* Python
* Streamlit
* NumPy
* Matplotlib

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Ashu27022011/Quadratic-solver-web.git
```

2. Move into the project folder:

```bash
cd Quadratic-solver-web
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
streamlit run app.py
```

> Replace `app.py` with your main Python file if it has a different name.

## How It Works

The application accepts the coefficients **a**, **b**, and **c** and solves the equation using the quadratic formula.

It also determines whether the roots are:

* Two distinct real roots
* One repeated real root
* Two complex roots

Finally, it plots the corresponding parabola for easy visualization.

## Example

Input:

```
a = 1
b = -5
c = 6
```

Output:

```
Roots:
x₁ = 3
x₂ = 2

Discriminant = 1
Nature of Roots = Two Distinct Real Roots
```

Along with a graph of the quadratic function.

## Project Structure

```
Quadratic-solver-web/
│
├── app.py
├── requirements.txt
├── README.md
├── assets/
└── ...
```

## Future Improvements

* Equation parser (accept equations like `2x² + 5x - 3 = 0`)
* Step-by-step solution
* Export results as PDF
* Dark/Light mode
* Mobile-friendly interface
* Support for cubic and higher-order equations

## Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Open a Pull Request.

## License

This project is open source and available under the MIT License.

## BY:

**Architects of a New World**

GitHub: https://github.com/Ashu27022011

**This readme and some bit of code is done by GPT so, beaware**
