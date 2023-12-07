#!/usr/bin/python3
"""Flask App"""
from models import storage
from models import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', states=all_states)


@app.teardown_appcontext
def drop_content(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
