#!/usr/bin/python3
""" review """
from flask import jsonify, abort, request
from models import storage
from models.place import Place
from models.review import Review
from models.user import User
from api.v1.views import app_views


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
@app_views.route('/places/<place_id>/reviews/', methods=['GET'])
def get_reviews(place_id):
    """
    review
    """
    list_review = []
    Place = storage.get(Place, place_id)
    if not Place:
        abort(404)
    for review in Place.reviews:
        list_review.append(review.to_dict())
    return jsonify(list_review)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review(review_id):
    """
    review
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """
    review
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def post_review(place_id):
    """
    review
    """
    Place = storage.get(Place, place_id)
    if not Place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if "user_id" not in data:
        abort(400, description="Missing user_id")
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if "text" not in data:
        abort(400, description="Missing text")
    new_review = Review(**data)
    new_review.place_id = Place.id
    new_review.save()
    return (jsonify(new_review.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def put_review(review_id):
    """
    review
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    keys_to_ignore = ["id", "place_id", "created_at", "updated_at"]
    for key, value in data.items():
        if key not in keys_to_ignore:
            setattr(review, key, value)
    storage.save()
    return (jsonify(review.to_dict()), 200)
