#!/usr/bin/python3
"""Flask App"""
from models import storage
from models import State, Amenity, Place
from os import getenv
from flask import Flask, render_template, url_for


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template('100-hbnb_filters.html', states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def drop_content(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
