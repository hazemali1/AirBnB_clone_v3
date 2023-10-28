#!/usr/bin/python3
""" City """
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State
from models.city import City
from api.v1.views import app_views

@app_views.route('/states')
@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_state(state_id=None):
    """
    state_id
    """
    list_state = []
    state = storage.get(State, state_id)

    list_state.append(state.to_dict())
    return jsonify(list_state)



