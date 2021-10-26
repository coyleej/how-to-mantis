"""Demonstrate working of pytest 

Modified from https://realpython.com/python-testing/ and
https://www.geeksforgeeks.org/unit-testing-python-unittest/
"""
import pytest

def test_strings_a(): 
    """Test if the string contains 4 a's."""
    assert "a"*4 == "aaaa"

def test_upper():         
    """Test if the string is now upper case."""
    assert "foo".upper() == "FOO"

def test_isupper():
    """Test if the string is uppercase."""
    assert "FOO".isupper() == True 
    assert "Foo".isupper() == False

def test_strip():         
    """Test if the string strips properly."""
    s = "geeksforgeeks"
    assert s.strip("geek") == "sforgeeks"

@pytest.mark.skip
def test_split():         
    """Test if the string splits properly.""" 
    s = "hello world"
    assert s.split() == ["hello", "world"] 

@pytest.mark.sum
def test_sum():
    """Check sum of a list."""
    assert sum([1, 2, 3]) == 6, "Should be 6"

@pytest.mark.xfail
def test_sum_tuple():
    """Check sum of a tuple."""
    assert sum((1, 2, 2)) == 6, "Should be 6" 

