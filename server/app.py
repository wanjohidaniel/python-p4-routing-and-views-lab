#!/usr/bin/env python3

from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f'<h1>{title}</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return Response(parameter, mimetype='text/plain')

@app.route('/count/<int:parameter>')
def count(parameter):
    count_list = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return Response(count_list, mimetype='text/plain')

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return Response('Invalid operation', status=400, mimetype='text/plain')

    return Response(str(result), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
