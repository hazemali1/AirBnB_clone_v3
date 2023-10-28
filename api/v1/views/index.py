#!/usr/bin/python3
"""
python3
"""
from api.v1.views import app_views
from flask import jsonify
"""
import flask
"""


@app_views.route('/status', strict_slashes=False)
def status():
    """
    status
    """
    return jsonify(status='OK')
