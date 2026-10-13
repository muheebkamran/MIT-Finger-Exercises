class Circle():
    def __init__(self, radius):
        """ Initializes self with radius """
        self.radius = radius

    def get_radius(self):
        """ Returns the radius of self """
        return self.radius

    def __add__(self, c):
        """ c is a Circle object 
        Returns a new Circle object whose radius is 
        the sum of self and c's radius """
        return Circle(self.radius + c.radius)
        

    def __str__(self):
        """ A Circle's string representation is the radius """
        return str(self.radius)

# test cases created by ai

# 1. Test Initialization and get_radius
c1 = Circle(5)
c2 = Circle(10)
print(f"c1 radius: {c1.get_radius()}")  # Expected: 5
print(f"c2 radius: {c2.get_radius()}")  # Expected: 10

# 2. Test String Representation (__str__)
print(f"c1 string: {c1}")  # Expected: "5"
print(f"c2 string: {c2}")  # Expected: "10"

# 3. Test Addition (__add__)
c3 = c1 + c2
print(f"c3 type: {type(c3)}")         # Expected: <class '__main__.Circle'>
print(f"c3 radius: {c3.get_radius()}")  # Expected: 15
print(f"c3 string: {c3}")              # Expected: "15"

# 4. Test Chained Addition
c4 = Circle(2)
c5 = c1 + c2 + c4
print(f"c5 radius: {c5.get_radius()}")  # Expected: 17