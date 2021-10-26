class Base():
    pass

class NoSuper(Base):
    """Does not use super()."""
    def __init__(self):
        Base.__init__(self)   # Avoid this!
        print("NoSuper init")

    def print_message(self):
        print("Hi! - Method inherited from NoSuper")

class UsesSuper(Base):
    """Uses super()."""
    def __init__(self):
        super().__init__()
        # Older syntax, works in Python 2 and 3:
        #super(UsesSuper, self).__init__()
        print("UsesSuper init")

    def print_message(self):
        print("Hi! - Method inherited from UsesSuper")


class UsesSuperEquiv(Base):
    """Demonstrate super()'s behavior."""
    def __init__(self):
        # Retrieve the method resolution order
        mro = type(self).mro()

        # Look at the parent classes; start with 
        # the immediately next one
        check_next = mro.index(UsesSuper) + 1
        while check_next < len(mro):
            next_class = mro[check_next]
            if '__init__' in next_class.__dict__:
                next_class.__init__(self)
                break
            check_next += 1
        print("UsesSuper init")

    def print_message(self):
        print("Hi! - Method inherited from UsesSuper")


class OtherClass(Base):
    """Another class."""
    def __init__(self):
        super(OtherClass, self).__init__()
        print("OtherClass init")

class TestNoSuper(NoSuper, OtherClass):
    """Does not use super()."""
    def __init__(self):
        Base.__init__(self)
        print("TestNoSuper init")

class TestUsesSuper(UsesSuper, OtherClass):
    """Uses super()."""
    def __init__(self):
        super().__init__()
        print("TestUsesSuper init")


print("Creating instance of TestNoSuper:")
test1 = TestNoSuper()
test1.print_message()

print("\nCreating instance of TestUsesSuper:")
test2 = TestUsesSuper()
test2.print_message()

