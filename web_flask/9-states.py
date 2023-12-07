#!/usr/bin/python3
"""Flask App"""
from models import storage
from models import State
from os import getenv
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_cities():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    all_states = storage.all(State).values()
    state = None
    for item in all_states:
        if item.id == id:
            state = item

    if state:
        cities = state.cities
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', state=None)


@app.teardown_appcontext
def drop_content(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
