#!/usr/bin/python3
<<<<<<< HEAD
"""starts a Flask web application that listens on 0.0.0.0, port 5000"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays 'HBNB'"""
=======
"""Starts Flask web app
Routes:
    / - display "Hello HBNB!"
    /hbnb - display "HBNB"
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_route():
    """prints Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """prints HBNB"""
>>>>>>> 269cb70efdd44736bfe5a03f9fc6aadc57c24591
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
