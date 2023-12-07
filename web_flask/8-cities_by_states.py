#!/usr/bin/python3
"""Flask App"""
from models import storage
from models import State
from os import getenv
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_cities():
    all_states = storage.all(State).values()
    return render_template('8-cities_by_states.html', all_states=all_states)


@app.teardown_appcontext
def drop_content(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
