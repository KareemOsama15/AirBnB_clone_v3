#!/usr/bin/python3
""" Test .get() and .count() methods
"""
import models
from models.state import State

# print("All objects: {}".format(models.storage.count()))
# print("State objects: {}".format(models.storage.count(State)))

# first_state_id = list(models.storage.all(State).values())[0].id
# print("First state: {}".format(models.storage.get(State, first_state_id)))

def func():
    states = models.storage.all(State).values()
    return states

print(func())
