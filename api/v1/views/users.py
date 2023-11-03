#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.engine.file_storage import class_dict
from models.user import User
"""
import flask
"""


@app_views.route('/users/', methods=['GET', 'POST'], strict_slashes=False)
def users():
    """
    users
    """
    if request.method == 'GET':
        li = []
        users = storage.all(User)
        for user in users.values():
            li.append(user.to_dict())
        return jsonify(li)
    if request.method == 'POST':
        req = request.get_json()
        if req is None:
            abort(400, 'Not a JSON')
        req_email = req.get("email")
        if req_email is None:
            abort(400, 'Missing email')
        req_password = req.get("password")
        if req_password is None:
            abort(400, 'Missing password')
        obj = User(**req)
        obj.save()
        return (jsonify(obj.to_dict()), 201)


@app_views.route('/users/<user_id>', methods=['GET', 'DELETE', 'PUT'])
def user_id(user_id=None):
    """
    user_id
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if request.method == 'GET':
        return jsonify(user.to_dict())
    if request.method == 'DELETE':
        storage.delete(user)
        storage.save()
        return (jsonify({}), 200)
    if request.method == 'PUT':
        req = request.get_json()
        if req is None:
            abort(400, 'Not a JSON')
        keys_to_ignore = ["id", "created_at", "updated_at", "email"]
        for key, value in req.items():
            if key not in keys_to_ignore:
                setattr(user, key, value)
        storage.save()
        return (jsonify(user.to_dict()), 200)
