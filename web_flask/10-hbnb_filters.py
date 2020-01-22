#!/usr/bin/python3
"""
    Starts a Flask web application to listen on 0.0.0.0:5000
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def all_states():
    """
    List of all states
    """
    states = storage.all("State")
    amenities = storage.all("Amenity")
    context = {'states': states, 'amenities': amenities}
    return render_template('10-hbnb_filters.html', **context)


@app.teardown_appcontext
def teardown_app(exception):
    """
        Closing the storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
