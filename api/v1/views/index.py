#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from flask import jsonify
from models import storage
"""
import flask
"""


@app_views.route('/status')
def status():
    """
    status
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """
    stats
    """
    dec = {}
    classes = storage.class_dict
    dec["amenities"] = storage.count(classes["Amenity"])
    dec["cities"] = storage.count(classes["City"])
    dec["places"] = storage.count(classes["Place"])
    dec["reviews"] = storage.count(classes["Review"])
    dec["states"] = storage.count(classes["State"])
    dec["users"] = storage.count(classes["User"])
    return jsonify(dec)
