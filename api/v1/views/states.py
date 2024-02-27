#!/usr/bin/python3
"""State Api"""
from flask import jsonify, abort, make_response
from api.v1.views import app_views
from models.state import State
from models import storage


@app_views.route("/states", methods=["GET"], strict_slashes=False)
def get_states():
    """method retrieves state objects in a list"""
    states = storage.all(State).values()
    return jsonify([state.to_dict() for state in states])


@app_views.route("/states/<state_id>", methods=["GET"], strict_slashes=False)
def get_state_id(state_id):
    """method retrieves state object based on id or 404 if not found"""
    state = storage.get(State, state_id)
    if not state:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route("/states/<state_id>", methods=["DELETE"], strict_slashes=False)
def delete_state(state_id):
    """method deletes state based on id or 404 if not found"""
    state = storage.get(State, state_id)
    if state:
        storage.delete(state)
        storage.save()
    else:
        abort(404)
    return make_response(jsonify({}), 200)
