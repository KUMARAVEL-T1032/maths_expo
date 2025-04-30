import numpy as np
import sympy as sp
from sympy.vector import CoordSys3D, Del


def perform_calculation(expression):
    try:
        # Replace common math symbols with Python equivalents
        expr = expression.replace('^', '**').replace('×', '*').replace('÷', '/')
        result = eval(expr, {'__builtins__': None}, 
                     {'sin': np.sin, 'cos': np.cos, 'tan': np.tan,
                      'sqrt': np.sqrt, 'log': np.log, 'exp': np.exp,
                      'pi': np.pi, 'e': np.e})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

def solve_matrix(matrix, operation):
    try:
        np_matrix = np.array(matrix, dtype=float)
        
        if operation == 'determinant':
            if np_matrix.shape[0] != np_matrix.shape[1]:
                return "Matrix must be square for determinant"
            return str(np.linalg.det(np_matrix))
            
        elif operation == 'inverse':
            if np_matrix.shape[0] != np_matrix.shape[1]:
                return "Matrix must be square for inverse"
            return str(np.linalg.inv(np_matrix).tolist())
            
        elif operation == 'rank':
            return str(np.linalg.matrix_rank(np_matrix))
            
        elif operation == 'transpose':
            return str(np_matrix.T.tolist())
            
        else:
            return "Unsupported operation"
            
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_derivative(expression, variable):
    try:
        x = sp.symbols(variable)
        expr = sp.sympify(expression)
        derivative = sp.diff(expr, x)
        return sp.latex(derivative)
    except Exception as e:
        return f"Error: {str(e)}"

def calculate_integral(expression, variable):
    try:
        x = sp.symbols(variable)
        expr = sp.sympify(expression)
        integral = sp.integrate(expr, x)
        return sp.latex(integral)
    except Exception as e:
        return f"Error: {str(e)}"



