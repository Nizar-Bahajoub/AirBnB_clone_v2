#!/usr/bin/python3
""" Script that starts a Flask web app """
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    if '_' in text:
        text = text.replace('_', ' ')
    return "C " + str(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text="is cool"):
    if '_' in text:
        text = text.replace('_', ' ')
    return "Python " + str(text)


@app.route("/number_template/<int:n>", strict_slashes=False)
def nember_template(n):
    return render_template('5-number.html', number=n)


@app.route("/number/<int:n>")
def dispaly_n(n):
    return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
