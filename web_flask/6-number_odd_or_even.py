#!/usr/bin/python3
"""
import
"""

from flask import Flask, render_template
"""
flask
"""


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    hbnb
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    hbnb
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """
    hbnb
    """
    t = ""
    for i in text:
        if i == '_':
            t += ' '
        else:
            t += i
    return "C " + t


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def text_p(text="is cool"):
    """
    hbnb
    """
    t = ""
    for i in text:
        if i == '_':
            t += ' '
        else:
            t += i
    return "Python " + t


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    hbnb
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_html_file(n):
    """
    hbnb
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_html_file_oe(n):
    """
    hbnb
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    """
    main
    """
    app.run(host='0.0.0.0', port=5000)
