#!/usr/bin/python3
""" Basic Hello HBNB Web App """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Simple Hbnb Function """
    return render_template('7-states_list.html', state_table=storage.all(State))


@app.teardown_appcontext
def teardown_app(exception):
    """ Simple Teardown """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
