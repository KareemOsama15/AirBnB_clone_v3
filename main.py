#!/usr/bin/python3
""" Test .get() and .count() methods
"""
import models
from models.state import State
from models.city import City
from models.place import Place
import json
import requests

# print("All objects: {}".format(models.storage.count()))
# print("State objects: {}".format(models.storage.count(State)))

# first_state_id = list(models.storage.all(State).values())[0].id
# print("First state: {}".format(models.storage.get(State, first_state_id)))

# def func():
#     states = models.storage.all(City).values()
#     return states

# print(func())


"""Testing file
"""


# if __name__ == "__main__":
#     """ POST /api/v1/states
#     """
#     r = requests.post("http://0.0.0.0:5050/api/v1/states/", data={ 'name': "NewState" }, headers={ 'Content-Type': "application/x-www-form-urlencoded" })
#     print(r.status_code)

"""Testing file
"""
# import json
# import requests

# if __name__ == "__main__":
#     """ verify http response header Access-Control-Allow-Origin
#     """
#     r = requests.get("http://0.0.0.0:5050/api/v1/states")
#     print(r.headers.get("Access-Control-Allow-Origin") == "0.0.0.0")

# ids = ['ad124633-a610-483f-862a-6f54dda19c6e', 'daa15c1b-9ca6-4042-85fd-bdb7a46d5862']
# places = [models.storage.get(Place, id) for id in ids]
places = models.storage.all(Place).values()
for place in places:
    amenity_id = '12e9ccb4-03e4-4f82-ac3d-4fc7e3ebfbfe' 
    if amenity_id in place.amenities:
        print(place.to_dict())
    # print(place.amenities)
