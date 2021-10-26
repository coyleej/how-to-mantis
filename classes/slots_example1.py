"""Demonstrate use of __slots__"""
from sys import getsizeof
from statistics import mean
import timeit

class Country:
    """Class without slots dunder."""
    def __init__(self, states, cities):
        self.states = states
        self.cities = cities

class CountrySlots:
    """Class with slots dunder."""
    __slots__ = ["states", "cities"]
    def __init__(self, states, cities):
        self.states = states
        self.cities = cities

def set_get_del_func(obj):
    """Function to set, get, and delete attributes"""
    def set_get_del():
        obj.cities = ["Chicago", "Portland", "Sacremento"]
        obj.cities
        del obj.cities
    return set_get_del

# Without slots
print("Without slots")
usa = Country(["New York", "Indiana"], ["NYC", "Indy"])
print(f"usa.states: {usa.states}")
print(f"__dict__: {usa.__dict__}")
print(f"getsizeof(usa) = {getsizeof(usa)} bytes")
print(f"getsizeof(usa.__dict__) = {getsizeof(usa.__dict__)} bytes")
print("Instantiation time: "
        +f"{mean(timeit.repeat(set_get_del_func(usa))):.5f} s")
usa.rivers = ["Miami", "Huron", "Ohio"]
print(f"Adding river attribute: {usa.rivers}")
print(f"__dict__: {usa.__dict__}")

# With slots
print("\nWith slots")
usa_slot = Country(["California", "Ohio"], ["LA", "Dayton"])
print(f"usa_slot.states: {usa_slot.states}")
print(f"__slots__: {usa_slot.__slots__}")
print(f"getsizeof(usa_slot) = {getsizeof(usa_slot)} bytes")
print(f"getsizeof(usa_slot.__slots__) = {getsizeof(usa_slot.__slots__)} bytes")
print("Instantiation time: "
        +f"{mean(timeit.repeat(set_get_del_func(usa_slots))):.5f} s")
usa.rivers = ["Hudson", "Wabash", "Potomac"]
print(f"Adding river attribute: {usa_slot.rivers}")

