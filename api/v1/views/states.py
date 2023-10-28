#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.engine.file_storage import class_dict
"""
import flask
"""


@app_views.route('/states')
def states():
    """
    states
		"""
    states = storage.all('State')
    for state in states.values():
        li.append(state)
    return jsonify(li)
