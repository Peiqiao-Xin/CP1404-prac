from flask import Flask, request, render_template, redirect, url_for
from recursion import factorial, fib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/factorial/<int:n>')
def fact(n):
    result = factorial(n)
    return f"Factorial of {n} is {result}"

@app.route('/fibonacci/<int:n>')
def fibonacci(n):
    sequence = fib(n)
    return f"Fibonacci sequence up to {n}: {sequence}"
