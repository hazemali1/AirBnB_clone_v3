#!/usr/bin/python3
"""
import app flask json
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.engine.file_storage import class_dict
from models.amenity import Amenity
from os import getenv
"""
import flask
"""


@app_views.route("places/<place_id>/amenities",methods=['GET'])
@app_views.route('/places/<place_id>/amenities/', methods=['GET'])
def get_amenities(place_id):
    """
    get amenities
    """
    list_amenities=[]
    placeID = storage.get(place, place_id)
    if not placeID:
        abort(404)
    for amnyobj in placeID.items():
        if amnyobj.id == place_id:
            for amny in amnyobj.amenities:
                list_amenities.append(amny.to_dict())
    return jsonify(list_amenities)


@app_views.route("places/<place_id>/amenities/<amenity_id>",methods=['DELETE'])
def del_amenities(place_id, amenity_id):
    """
    del amenities
    """
    place = storage.get(Place, place_id)
    amenity = storage.get(Amenity, amenity_id)

    if place is None or amenity is None:
        abort(404)

    if amenity not in place.amenities:
        abort(404)
    for amnyobj in placeID.items():
        if amnyobj.id == place_id:
            if amnyobj.amenities == []:
                    abort(404)
            for amenity in amnyobj.amenities:
                if amenity.id == amenity_id:
                    storage.delete(amenity)
                    storage.save()
    storage.save()
    return jsonify({}), 200


@app_views.route('/places/<place_id>/amenities/<amenity_id>',
                methods=['POST'])
def create_amenities(place_id, amenity_id):
    """
    Link a Amenity object to a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    amenity = storage.get(Amenity, amenity_id)

    if not amenity:
        abort(404)

    for amnyobj in placeID.items():
        if amnyobj.id == place_id:
            for amny in amnyobj.amenities:
                return make_response(jsonify((amny.id).to_dict), 200)
    return make_response[jsonify(amenity),201]
