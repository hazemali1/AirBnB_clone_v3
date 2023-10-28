#!/usr/bin/python3
""" City """
from api.v1.views import app_views
from flask import jsonify, abort, make_response, request
from models import storage
from models.state import State
from models.city import City


@app_views.route('/api/v1/states/<state_id>/cities', methods=['GET'])
def cities(state_id):
    list_city = []
    stateId = storage.get(state, state_id)
    if not state_id:
        abort(404)
    for c in stateId.cities:
        list_city.append(c.to_dict())
    jsonify(list_city)


@app_views.route('/api/v1/cities/<city_id>', methods=['GET'])
def city(city_id):
    cityId = storage.get(state, city_id)
    if not city_id:
        abort(404)
    return jsonify(cityId.to_dict())


@app_views.route('/api/v1/cities/<city_id>', methods=['DELETE'])
def Dcity(city_id):
    cityId_delete = storage.get(state, city_id)
    if not cityId_delete:
        abort(404)
    storage.delete(cityId_delete)
    storage.save()
    return make_response[jsonify({}), 200]


@app_views.route('/api/v1/states/<state_id>/cities', methods=['POST'])
def potscity(state_id):
    stateId_post = storage.get(state, state_id)
    if not stateId_post:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if "name" not in request.get_json():
        abort(400, description="Missing name")
    d = request.get_json()
    ncity = City(**d)
    ncity.state.id = stateId_post
    ncity.save()
    return make_response[jsonify(ncity.to_dict()), 201]


@app_views.route(' /api/v1/cities/<city_id>', methods=['POST'])
def putcity(city_id):
    cityId_put = storage.get(City, city_id)
    if not city_id:
        abort(404)
    if not request.get_json():
        abort(400, description="Not a JSON")
    if "name" not in request.get_json():
        abort(400, description="Missing name")
    d = request.get_json()
    keys_to_ignore = ["id", "state_id", "created_at", "updated_at"]
    for k, v in d.items():
        if k not in keys_to_ignore:
            setattr(city, key, value)
    storage.save()
    return make_response[jsonify(ncity.to_dict()), 201]
