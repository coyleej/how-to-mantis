"""Demonstrate working of unittest 

Modified from https://www.geeksforgeeks.org/unit-testing-python-unittest/
"""
import unittest 
  
class TestStringMethods(unittest.TestCase): 
      
    def test_strings_a(self): 
        """Test if the string contains 4 a's."""
        self.assertEqual( "a"*4, "aaaa") 
  
    def test_upper(self):         
        """Test if the string is now upper case."""
        self.assertEqual("foo".upper(), "FOO") 
  
    def test_isupper(self):
        """Test if the string is uppercase."""
        self.assertTrue("FOO".isupper()) 
        self.assertFalse("Foo".isupper()) 
  
    def test_strip(self):         
        """Test if the string strips properly."""
        s = "geeksforgeeks"
        self.assertEqual(s.strip("geek"), "sforgeeks") 
  
    def test_split(self):         
        """Test if the string splits properly.""" 
        s = "hello world"
        self.assertEqual(s.split(), ["hello", "world"]) 
  
if __name__ == "__main__": 
    unittest.main()
