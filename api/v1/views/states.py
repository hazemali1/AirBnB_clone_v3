#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.engine.file_storage import class_dict
from models.state import State
"""
import flask
"""


@app_views.route('/states')
def states():
    """
    states
		"""
    li = []
    states = storage.all(State)
    for state in states.values():
        li.append(state.to_dict())
    return jsonify(li)


@app_views.route('/states/<state_id>')
def states_id(state_id=None):
    """states_id"""
    li = []
    states = storage.all(State)
    for state in states.values():
        if state.id == state_id:
            li.append(state.to_dict())
    if len(li):
        return jsonify(li)
    else:
        abort(404)
