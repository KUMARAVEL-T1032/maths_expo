from flask import Flask, render_template, request
import numpy as np
import sympy as sp
from math_operations import *
from flask import Flask, render_template, request, jsonify
from sympy import symbols, diff, integrate, limit, sympify, oo


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('intex.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route('/matrix')
def matrix():
    return render_template('matrix.html')



@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/algebra', methods=['GET', 'POST'])
def algebra():
    result = None
    expression = ''
    operation = ''
    if request.method == 'POST':
        expression = request.form.get('expression')
        variable = request.form.get('variable', 'x')
        operation = request.form.get('operation')

        try:
            expr = sp.sympify(expression)
            if operation == 'simplify':
                result = sp.simplify(expr)
            elif operation == 'expand':
                result = sp.expand(expr)
            elif operation == 'factor':
                result = sp.factor(expr)
            elif operation == 'solve':
                result = sp.solve(expr)
            elif operation == 'derive':
                result = sp.diff(expr, sp.Symbol(variable))
            elif operation == 'integrate':
                result = sp.integrate(expr, sp.Symbol(variable))
            else:
                result = "Invalid operation"
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template('algebra.html', result=result, expression=expression, operation=operation)
@app.route('/calculus')
def calculas():
    return render_template('calculus.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    operation = data.get('operation')
    expr = sympify(data.get('expression'))
    var = symbols(data.get('variable', 'x'))

    try:
        if operation == 'derivative':
            result = diff(expr, var)
        elif operation == 'integral':
            result = integrate(expr, var)
        elif operation == 'limit':
            point = data.get('point')
            if point == 'inf':
                point = oo
            elif point == '-inf':
                point = -oo
            else:
                point = sympify(point)
            result = limit(expr, var, point)
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': str(result)})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
