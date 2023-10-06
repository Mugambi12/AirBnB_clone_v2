#!/usr/bin/python3
"""A script that start web application with two routings
"""

from flask import Flask
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
    """Return start with c and replace _ with space
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Return string start with Python and replace _ with space
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
