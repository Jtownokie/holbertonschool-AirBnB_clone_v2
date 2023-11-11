#!/usr/bin/python3
""" Basic Hello HBNB Web App """
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Simple Hello Function """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Simple Hbnb Function """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Simple Hbnb Function """
    return f'C {text.replace("_", " ")}'


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ Simple Hbnb Function """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Simple Hbnb Function """
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Simple Hbnb Function """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
