#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application that listens on 0.0.0.0, port 5000"""

from models import storage
from models.state import State
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with a list of all State objects.
    /states/<id>: HTML page displaying the given state with <id>.
"""
from models import storage
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
from flask import Flask
from flask import render_template

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """for /states route: displays a HTML page: (inside the <body> tag)
       -> h1: "States"
       -> ul: list of all 'State' objects present in 'DBStorage'
              sorted by name (A-Z)
            -> li: description of one 'State':
                   "<state.id>: <b><state.name><b>"

       for /states/<id> route: displays a HTML page: (inside the <body> tag)
       if a 'State' object is found with this 'id':
       -> h1: "State"
       -> h3: "Cities:"
            -> ul: list of 'City' objects linked to the 'State'
                   sorted by name (A->Z)
            -> li: description of one 'City':
                   "<city.id>: <b><city.name></b>"
       otherwise:
       -> h1: "Not found!"
    """
    states = storage.all(State)
    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template("9-states.html", states=states, state_id=state_id)
=======
@app.route("/states", strict_slashes=False)
def states():
    """Displays an HTML page with a list of all States.
    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591


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
