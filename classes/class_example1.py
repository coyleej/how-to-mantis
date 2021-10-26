class Complex:
    """Demonstrate class behavior"""
    x = 1
    def __init__(self, real_part, imag_part):
        """Customize default instantiation"""
        self.r = real_part
        self.i = imag_part

    def conjugate(self):
        """Find the comples conjugate"""
        self.i *= -1

    def display_value(self):
        """Display the current value"""
        print(f"{self.r} + {self.i}i")

comp1 = Complex(3, 4)
comp2 = Complex(5, 9)

print(f"comp1.x: {comp1.x}")
print(f"comp2.x: {comp2.x}")
comp1.display_value()
comp2.display_value()

print("\n\n")
################ BASICS ################ 

# Attribute reference
print(f"{Complex.x}")

# Instantiation
comp = Complex(3, 4)

# Attribute references on instance
print(f"{comp.r} + {comp.i}i")
comp.r = 5
comp.display_value()
comp.conjugate()
comp.display_value()

# Add new attribute to instance
comp.test = 9
print(f"Added attribute test: {comp.test}")


