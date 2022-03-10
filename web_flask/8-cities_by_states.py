#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application that listens on 0.0.0.0, port 5000"""

from models import storage
from models.state import State
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with a list of all states and related cities.
"""
from models import storage
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
<<<<<<< HEAD
    """displays a HTML page: (inside the <body> tag)
       -> h1: "States"
       -> ul: list of all 'State' objects present in 'DBStorage'
              sorted by name (A-Z)
            -> li: description of one 'State':
                   "<state.id>: <b><state.name><b>"
                -> ul: list of 'City' objects linked to the 'State'
                       sorted by name (A->Z)
                    -> li: description of one 'City':
                           "<city.id>: <b><city.name></b>"
    """
    states = storage.all(State)
=======
    """Displays an HTML page with a list of all states and related cities.
    States/cities are sorted by name.
    """
    states = storage.all("State")
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
<<<<<<< HEAD
    """removes the current SQLAlchemy session"""
=======
    """Remove the current SQLAlchemy session."""
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
