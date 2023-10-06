#!/usr/bin/python3
"""A script that start web application with multiple routings
"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello():
    """Return Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Return HBNB
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Return string that start with C and replace _ with space
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Return string that start with Python and replace _ with space
    """
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>')
def number(n=None):
    """Allow request if path variable is a valid integer
    """
    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    """Retrieve template requested
    """
    path = '5-number.html'
    return render_template(path, n=n)


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
