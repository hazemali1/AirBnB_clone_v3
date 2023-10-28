#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from models import storage
from flask import jsonify
"""
import flask
"""


@app_views.route('/status', strict_slashes=False)
def status():
    """
    status
    """
    return jsonify(
        {
            "status": "OK"
        }
    )


@app_views.route('/api/v1/stats', strict_slashes=False)
def stats():
    """
    stats
    """
    return
