#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.engine.file_storage import class_dict
from models.amenity import Amenity
"""
import flask
"""


@app_views.route('/amenities/', methods=['GET', 'POST'], strict_slashes=False)
def amenities():
    """
    amenities
    """
    if request.method == 'GET':
        li = []
        amenities = storage.all(Amenity)
        for amenitie in amenities.values():
            li.append(amenitie.to_dict())
        return jsonify(li)
    if request.method == 'POST':
        req = request.get_json()
        if req is None:
            abort(400, 'Not a JSON')
        req_name = req.get("name")
        if req_name is None:
            abort(400, 'Missing name')
        obj = Amenity(**req)
        obj.save()
        return (jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>', methods=['GET', 'DELETE', 'PUT'])
def amenity_id(amenity_id=None):
    """amenity_id"""
    amenitie = storage.get(Amenity, amenity_id)
    if amenitie is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(amenitie.to_dict())
    if request.method == 'DELETE':
        storage.delete(amenitie)
        storage.save()
        return (jsonify({}), 200)
    if request.method == 'PUT':
        req = request.get_json()
        if req is None:
            abort(400, 'Not a JSON')
        keys_to_ignore = ["id", "created_at", "updated_at"]
        for key, value in req.items():
            if key not in keys_to_ignore:
                setattr(amenitie, key, value)
        storage.save()
        return (jsonify(amenitie.to_dict()), 200)
