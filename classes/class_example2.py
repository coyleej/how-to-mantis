class TestClass:
    """Demonstrate instance and class methods."""
    def create_arr(self):
        """Create an array."""
        self.arr = []
    
    def insert_to_arr(self, value):
        """Add an element to an array."""
        self.arr.append(value)
        
    @classmethod
    def class_method(cls):
        print("The class method was called.")

TestClass.class_method()

test = TestClass()
test.create_arr()
test.insert_to_arr(1)
test.insert_to_arr(2)
test.insert_to_arr(3)
print(test.arr)


