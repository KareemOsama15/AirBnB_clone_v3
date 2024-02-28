#!/usr/bin/python3
"""Place Api"""
from flask import jsonify, abort, make_response, request
from api.v1.views import app_views
from models.place import Place
from models.city import City
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.user import User
from models import storage


@app_views.route("/cities/<city_id>/places", methods=['GET'],
                 strict_slashes=False)
def get_places(city_id):
    """retrieve list of all places in city"""
    if not storage.get(City, city_id):
        abort(404)
    places = storage.all(Place).values()
    all_places = []
    for place in places:
        if place.city_id == city_id:
            all_places.append(place.to_dict())
    return jsonify(all_places)


@app_views.route("/places/<place_id>", methods=['GET'],
                 strict_slashes=False)
def get_place(place_id):
    """Retrieve place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>", methods=['DELETE'],
                 strict_slashes=False)
def delete_place(place_id):
    """Deletes a place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    storage.delete(place)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route("/cities/<city_id>/places", methods=['POST'],
                 strict_slashes=False)
def create_place(city_id):
    """Create a new Place"""
    if not storage.get(City, city_id):
        abort(404)

    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json' or not request.get_json():
        abort(400, 'Not a JSON')

    place_data = request.get_json()
    if 'user_id' not in place_data:
        abort(400, 'Missing user_id')
    elif not storage.get(User, place_data['user_id']):
        abort(404)
    elif 'name' not in place_data:
        abort(400, 'Missing name')

    place_data['city_id'] = city_id
    new_place = Place(**place_data)
    new_place.save()
    return make_response(jsonify(new_place.to_dict()), 201)


@app_views.route("/places/<place_id>", methods=['PUT'],
                 strict_slashes=False)
def update_place(place_id):
    """Update a Place"""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)

    content_type = request.headers.get('Content-Type')
    if content_type != 'application/json' or not request.get_json():
        abort(400, 'Not a JSON')

    place_data = request.get_json()
    ignored_keys = ['id', 'created_at', 'updated_at', 'user_id', 'city_id']
    for key, value in place_data.items():
        if key not in ignored_keys:
            setattr(place, key, value)
    storage.save()
    return make_response(jsonify(place.to_dict()), 200)


@app_views.route("/places_search", methods=['POST'],
                 strict_slashes=False)
def places_search():
    """Search on Places"""
    content_type = request.headers.get('Content-Type')
    places_data = request.get_json()
    if content_type != 'application/json' or not places_data:
        abort(400, 'Not a JSON')

    if len(places_data) == 0:
        return jsonify([place.to_dict] for place in storage.all(Place).values())

    all_places = []
    all_cities = []
    places_ojbs = []
    places = storage.all(Place).values()

    for key, list_value in places_data.items():
        if key == 'states':
            for state_id in list_value:
                state = storage.get(State, state_id)
                if state:
                    all_cities.append(city.city_id for city in state.cities)
        elif key == 'cities':
            for city_id in all_cities:
                if city_id not in list_value:
                    list_value.append(city_id)
            for city_id in list_value:
                if storage.get(City, city_id):
                    for place in places:
                        if place.city_id == city_id:
                            places_ojbs.append(place)
        elif key == 'amenities':
            if len(list_value) != 0:
                for amenity_id in list_value:
                    amenity = storage.get(Amenity, amenity_id)
                    if amenity:
                        for place in places_ojbs:
                            if amenity.place_id == place.id:
                                all_places.append(place.to_dict())
            else:
                for place in places_ojbs:
                    all_places.append(place.to_dict())
    return jsonify(all_places)
