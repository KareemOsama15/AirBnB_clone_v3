#!/usr/bin/python3
""" Test .get() and .count() methods
"""
import models
from models.state import State
from models.city import City
import json
import requests

# print("All objects: {}".format(models.storage.count()))
# print("State objects: {}".format(models.storage.count(State)))

# first_state_id = list(models.storage.all(State).values())[0].id
# print("First state: {}".format(models.storage.get(State, first_state_id)))

def func():
    states = models.storage.all(City).values()
    return states

print(func())


"""Testing file
"""


# if __name__ == "__main__":
#     """ POST /api/v1/states
#     """
#     r = requests.post("http://0.0.0.0:5050/api/v1/states/", data={ 'name': "NewState" }, headers={ 'Content-Type': "application/x-www-form-urlencoded" })
#     print(r.status_code)
