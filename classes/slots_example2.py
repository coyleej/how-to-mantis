"""Demonstrate inheritance with __slots__"""
from sys import getsizeof, version

print("Planet class")
class Planet:
    """Define parent class with slots."""
    __slots__ = ("name",)

planets = Planet()
planets.name = ["Jupiter", "Earth", "Pluto"]


print("\nEarth class")
class Earth(Planet):
    """Show what happens when inheriting slots dunder.

    Anything inherited from a parent class that used slots
    is still in slots. New attributes are added to dict.
    """
    pass

home_planet = Earth()
print(home_planet.__slots__)
home_planet.name = ["Earth"]
home_planet.cities = ["DC", "Tokyo", "Paris"]
home_planet.countries = ["USA", "Japan", "France"]
print(home_planet.__dict__)


print("\nPluto class (empty child class slots dunder)")
class Pluto(Planet):
    """Show what happens when child class set slots dunder.

    You can't create any new attributes or access attributes
    inherited from the parent class.
    """
    __slots__ = ()

was_a_planet = Pluto()
print(was_a_planet.__slots__)
#print(was_a_planet.__dict__)   # AttributeError
#print(was_a_planet.name)       # AttributeError
#was_a_planet.x = 1             # AttributeError


print("\nMars class (dynamic)")
class Mars(Planet):
    """Use slots and make child class instance dynamic.
    
    Users can create any attribute they want if they add
    __dict__ to __slots__, but can't access attributes 
    inherited from parent class.
    """
    __slots__ = ("rovers", "__dict__")


red_planet = Mars()
red_planet.name = "Mars"
red_planet.rovers = "Curiousity"
red_planet.weather = "dusty"
print(red_planet.__slots__)
print(red_planet.__dict__)


print("\nNeptune class (doubly assigned attribute)")
class Neptune(Planet):
    """Assign attribute in both parent and child.
    
    No errors, but will take up more space than necessary.
    """
    __slots__ = ("name", "temp")

poseidon_planet = Neptune()
print("Size (bytes) when doubly assigned")
print(getsizeof(poseidon_planet))

class Neptune(Planet):
    """Not assign attribute in both parent and child."""
    __slots__ = ("temp")

poseidon_planet = Neptune()
print("Size (bytes) when not doubly assigned")
print(getsizeof(poseidon_planet))


print("\nElon Musk class (inherit both Earth and Mars)")
class ElonMusk(Earth, Mars):
    """Inherit multiple classes with slots.
    
    Inheriting more than one class with __slots__ defined 
    works in Python 3.7, but Python 3.8 definitely gives a
    TypeError when trying to define such a class. For this
    to work in Python 3.8+, one of the parents must define
    __slots__ as an empty tuple.
    """
    __slots__ = ()

that_guy = ElonMusk()
that_guy.name = "Elon"
that_guy.rovers = "Yup"
that_guy.water = "Yup"
print(that_guy.__slots__)
print(that_guy.__dict__)
print("Python", version)
