#!/usr/bin/python3
"""
    Starts a Flask web application to listen on 0.0.0.0:5000
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def all_states():
    """
    List all states
    """
    states = storage.all("State")
    context = {'route': 'all_states', 'states': states}
    return render_template('9-states.html', **context)


@app.route('/states/<id>')
def state_by_id(id):
    """
    List state by id
    """
    result = storage.all("State")
    try:
        states = result['State.{}'.format(id)]
        context = {'route': 'state_by_id', 'states': states}
        return render_template('9-states.html', **context)
    except KeyError:
        context = {'route': 'state_by_id', 'states': None}
        return render_template('9-states.html', **context)


@app.teardown_appcontext
def teardown_app(exception):
    """
        Closing the storage
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
