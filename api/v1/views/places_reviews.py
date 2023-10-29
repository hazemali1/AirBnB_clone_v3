#!/usr/bin/python3
""" Review """
from flask import jsonify, abort, make_response, request
from models import storage
from models.Place import Place
from models.Review import Review
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_reviews(place_id):
    """
    Review
    """
    list_Review = []
    Place = storage.get(Place, place_id)
    if not Place:
        abort(404)
    for Review in Place.reviews:
        list_Review.append(Review.to_dict())
    return jsonify(list_Review)


@app_views.route('/reviews/<Review_id>', methods=['GET'], strict_slashes=False)
def get_Review(Review_id):
    """
    Review
    """
    Review = storage.get(Review, Review_id)
    if not Review:
        abort(404)
    return jsonify(Review.to_dict())


@app_views.route('/reviews/<Review_id>', methods=['DELETE'], strict_slashes=False)
def delete_Review(Review_id):
    """
    Review
    """
    Review = storage.get(Review, Review_id)
    if not Review:
        abort(404)
    storage.delete(Review)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_Review(place_id):
    """
    Review
    """
    Place = storage.get(Place, place_id)
    if not Place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if "name" not in data:
        abort(400, description="Missing name")
    new_Review = Review(**data)
    new_Review.place_id = Place.id
    new_Review.save()
    return make_response(jsonify(new_Review.to_dict()), 201)


@app_views.route('/reviews/<Review_id>', methods=['PUT'], strict_slashes=False)
def put_Review(Review_id):
    """
    Review
    """
    Review = storage.get(Review, Review_id)
    if not Review:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    keys_to_ignore = ["id", "place_id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in keys_to_ignore:
            setattr(Review, key, value)
    storage.save()
    return make_response(jsonify(Review.to_dict()), 200)
