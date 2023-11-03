#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.engine.file_storage import class_dict
from models.state import State
"""
import flask
"""


@app_views.route('/states/', methods=['GET', 'POST'], strict_slashes=False)
def states():
    """
    states
    """
    if request.method == 'GET':
        li = []
        states = storage.all(State)
        for state in states.values():
            li.append(state.to_dict())
        return jsonify(li)
    if request.method == 'POST':
        req = request.get_json()
        if req is None:
            abort(400, 'Not a JSON')
        req_name = req.get("name")
        if req_name is None:
            abort(400, 'Missing name')
        obj = State(**req)
        obj.save()
        return (jsonify(obj.to_dict()), 201)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE', 'PUT'])
def states_id(state_id=None):
    """states_id"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(state.to_dict())
    if request.method == 'DELETE':
        storage.delete(state)
        storage.save()
        return (jsonify({}), 200)
    if request.method == 'PUT':
        req = request.get_json()
        if req is None:
            abort(400, 'Not a JSON')
        keys_to_ignore = ["id", "created_at", "updated_at"]
        for key, value in req.items():
            if key not in keys_to_ignore:
                setattr(State, key, value)
        storage.save()
        return (None, 200)
