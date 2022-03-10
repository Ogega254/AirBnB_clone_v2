#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application that listens on 0.0.0.0, port 5000"""

from models import storage
from models.state import State
=======
"""Starts a flask app
    listens to 0.0.0.0:5000
    
"""
from models import storage
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
<<<<<<< HEAD
    """displays a HTML page: (inside the <body> tag)
       -> h1: "States"
       -> ul: list of all 'State' objects present in 'DBStorage'
              sorted by name (A-Z)
            -> li: description of one 'State':
                   "<state.id>: <b><state.name><b>"
    """
    states = storage.all(State)
=======
    """Displays an HTML page with a list of all State objects in DBStorage.
    States are sorted by name.
    """
    states = storage.all("State")
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
    return render_template("7-states_list.html", states=states)


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
