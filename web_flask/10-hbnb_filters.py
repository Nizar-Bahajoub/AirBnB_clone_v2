#!/usr/bin/python3
"""Flask App"""
from models import storage
from models import State, Amenity
from os import getenv
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def drop_content(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
