#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5555, debug=True)

@app.route('/')
def index():
    return f"<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f"{parameter}"

@app.route('/count/<parameter>')
def count(parameter):
    num_display = ""
    for num in range(int(parameter)):
        num_display = num_display + f"{num}\n"
    return num_display

@app.route('/math/<num1>/<operation>/<num2>')
def math(num1, operation, num2):
    numA = int(num1)
    numB = int(num2)
    if operation == '+':
        return str(numA + numB)
    elif operation == '-':
        return str(numA - numB)
    elif operation == '*':
        return str(numA * numB)
    elif operation == 'div':
        return str(numA / numB)
    elif operation == '%':
        return str(numA % numB)

    