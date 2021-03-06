#!/usr/bin/python3
"""
    Starts a Flask web application to listen on 0.0.0.0:5000
"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """
        Display Hello HBNB!
    """
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """
        Route /hbnb: display “HBNB”
    """
    return ("HBNB")


@app.route('/c/<text>')
def c(text):
    """
        Replace underscore _ symbols with a space
    """
    return ("C {}".format(text.replace('_', ' ')))


@app.route('/python')
@app.route('/python/<text>')
def python(text="is cool"):
    """
        Default text added: "is cool"
        Replace underscore _ symbols with a space
    """
    return ("Python {}".format(text.replace('_', ' ')))


@app.route('/number/<int:n>')
def number(n):
    """
        Displays n is a number only if n is an integer
    """
    return ("{:d} is a number".format(n))


@app.route('/number_template/<int:n>')
def ntemplate(n):
    """
        Display a HTML page only if n is an integer
    """
    return (render_template('5-number.html', n=n))


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    """
        Display a HTML page only if n is an integer and inside of the body
        if the number is odd or even
    """
    return (render_template('6-number_odd_or_even.html', n=n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
