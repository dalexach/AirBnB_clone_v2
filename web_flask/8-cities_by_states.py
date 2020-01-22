#!/usr/bin/python3
"""
    Starts a Flask web application to listen on 0.0.0.0:5000
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """
        List of cities and states in jinja template
    """
    all_states = storage.all("State")
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def teardown_app(exception):
    """
        Closing the storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
