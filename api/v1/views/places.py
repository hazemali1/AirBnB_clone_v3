#!/usr/bin/python3
""" Place """
from flask import jsonify, abort, make_response, request
from models import storage
from models.place import Place
from models.city import City
from api.v1.views import app_views


@app_views.route('/cities/<city_id>/places', methods=['GET'])
def get_places(city_id):
    """
    places
    """
    list_place = []
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    for place in city.places:
        list_place.append(place.to_dict())
    return jsonify(list_place)


@app_views.route('/places/<place_id>', methods=['GET'], strict_slashes=False)
def get_palce(place_id):
    """
    place
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route('/places/<place_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """
    place
    """
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/cities/<city_id>/places', methods=['POST'])
def post_place(city_id):
    """
    place
    """
    city = storage.get(City, city_id)
    if not city:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if "name" not in data:
        abort(400, description="Missing name")
    if "user_id" not in data:
        abort(400, description="Missing user_id")
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    new_place = Place(**data)
    new_place.city_id = city.id
    new_place.save()
    return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route('/places/<place_id>', methods=['PUT'], strict_slashes=False)
def put_place(place_id):
    """
    place
    """
    place = storage.get(Place, city_id)
    if not place:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    keys_to_ignore = ["id", "user_id", "created_at", "updated_at", "city_id"]
    for key, value in data.items():
        if key not in keys_to_ignore:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)


@app_views.route('/places_search', methods=['POST'], strict_slashes=False)
def search_places():
    """
    search_places
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"})
    if data and len(data):
        states = storage.get("states", None)
        cities = storage.get("cities", None)
        amenities = storage.get("amenities", None)

    if not data or not len(data) or (
                                    not states and
                                    not cities and
                                    not amenities):
        places = storage.all(Place).values()
        list_places = []
        for place in places:
            list_places.append(place.to_dict())
        return jsonify(list_places)

    list_places = []
    if states:
        states_obj = [storage.get(State, state_id) for state_id in states]
        for state in states_obj:
            if state:
                for city in state.cities:
                    if city:
                        for place in city.places:
                            list_places.append[place]

    if cities:
        cities_obj = [storage.get(City, cities_id) for cities_id in cities]
        for city in cities_obj:
            if city:
                for place in city.places:
                    if place:
                        list_places.append(place)

    if amenities:
        if not list_places:
            list_places = storage.all(Place).values()
        amenities_obj = [storage.get(Amenity, a_id) for a_id in amenities]
        list_places = [place for place in list_places
                       if all([am in place.amenities
                               for am in amenities_obj])]

    places = []
    for p in list_places:
        d = p.to_dict()
        d.pop('amenities', None)
        places.append(d)

    return jsonify(places)
