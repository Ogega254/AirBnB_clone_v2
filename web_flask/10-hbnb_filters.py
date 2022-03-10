#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application that listens on 0.0.0.0, port 5000"""

from models import storage
from models.state import State
from models.amenity import Amenity
=======
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page.
"""
from models import storage
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
from flask import Flask
from flask import render_template

app = Flask(__name__)


<<<<<<< HEAD
@app.route('/hbnb_filters', strict_slashes=False)
def filters():
    """displays a HTML page like '6-index.html' from static"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('10-hbnb_filters.html',
=======
@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays the main HBnB filters HTML page."""
    states = storage.all("State")
    amenities = storage.all("Amenity")
    return render_template("10-hbnb_filters.html",
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
                           states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(exc):
<<<<<<< HEAD
    """removes the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
=======
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
