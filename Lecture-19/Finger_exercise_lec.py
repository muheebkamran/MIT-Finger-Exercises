import random
class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
    def __str__(self):
        return "animal:"+str(self.name)+":"+str(self.age)
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, newage):
        self.age = newage
    def set_name(self, newname=""):
        self.name = newname

class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        self.set_name(name)
        self.friends = []
    def get_friends(self):
        return self.friends.copy()
    def speak(self):
        print("hello")
    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)

class Student(Person):
    def __init__(self, name, age, major=None):
        Person.__init__(self, name, age)
        self.major = major
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)
    def change_major(self, major):
        self.major = major
    def speak(self):
        r = random.random()
        if r < 0.25:
            print("--> i have homework")
        elif 0.25 <= r < 0.5:
            print("--> i need sleep")
        elif 0.5 <= r < 0.75:
            print("--> i should eat")
        else:
            print("--> i'm zooming")

##################################################
######### AT HOME ###############
##################################################
# Write the class Employee as a subclass of Person
class Employee(Person):
    """ An Employee contains an extra data attribute, salary as an int """
    def __init__(self, name, age, salary=0):
        """ initializes self as a Person with a salary data attribute, initially 0 """
        Person.__init__(self, name, age)
        self.salary = salary
        self.salaries = [salary]

    def get_salary(self):
        """ returns self's salary """
        return self.salary

    def set_salary(self, s):
        """ s is an int
        Sets self's salary data attribute to s """
        self.salary = s
        self.salaries.append(self.salary)
        return self.salary

    def salary_change(self, n):
        """ n is an int (positive or negative)
        Adds n to self's salary. If the result is negative, sets 
        self's salary to 0. Otherwise sets self's salary to the new value. """
        self.salary += (n)
        if self.salary <= 0:
            self.salary = 0
        self.salaries.append(self.salary)
        return self.salary

    def has_friends(self):
        """ Returns True if self's friend list is empty and False otherwise """
        if len(self.friends) > 0:
            return True
        else:
            return False

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def past_salaries_list(self):
        """ Keeps track of all salaries self has had in the order they've changed. 
        i.e. whenever the salary changes, keep track of it.
        Hint: you may need to add an additional data attribute to Employee.
        Returns a copy of the list of all salaries self has had, in order. """
        l = []
        for i in self.salaries:
            l.append(i)
        return l

    def past_salary_freq(self):
        """ Returns a dictionary where the key is a salary number and the 
        value is how many times self's salary has changed to that number. """
        d = {}
        x = self.past_salaries_list()
        for i in x:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        return d
# -----------------------------
# Testing
# -----------------------------
    
e = Employee("ana", 35)
print(e.get_salary())   # prints 0
e.set_salary(1000)
print(e.get_salary())   # prints 1000
e.salary_change(2000)
print(e.get_salary())   # prints 3000
e.salary_change(-50000)
print(e.get_salary())   # prints 0
print(e.has_friends())  # prints False
e.add_friend("bob")
print(e.has_friends())  # prints True
print(e.past_salaries_list())  # prints [0, 1000, 3000, 0]
print(e.past_salary_freq())  # prints {0: 2, 1000: 1, 3000: 1}

# -----------------------------
# Animal Tests
# -----------------------------
a = Animal(4)
print(a)                # prints animal:None:4
print(a.get_age())      # prints 4
print(a.get_name())     # prints None
a.set_age(5)
print(a.get_age())      # prints 5
a.set_name("fido")
print(a.get_name())     # prints fido
print(a)                # prints animal:fido:5

# -----------------------------
# Person Tests
# -----------------------------
p1 = Person("john", 30)
p2 = Person("mary", 25)
print(p1)               # prints person:john:30
print(p1.get_name())    # prints john
print(p1.get_age())     # prints 30
p1.speak()              # prints hello
p1.age_diff(p2)         # prints 5 year difference
print(p1.get_friends()) # prints []
p1.add_friend("mary")
p1.add_friend("mary")   # duplicate; should not be added again
print(p1.get_friends()) # prints ['mary']

# -----------------------------
# Student Tests
# -----------------------------
s = Student("alice", 20, "CS")
print(s)                # prints student:alice:20:CS
print(s.get_name())     # prints alice
print(s.get_age())      # prints 20
print(s.major)          # prints CS
s.change_major("Math")
print(s)                # prints student:alice:20:Math
s.speak()               # prints a random message (e.g., "--> i have homework")

# -----------------------------
# Employee Tests
# -----------------------------
e = Employee("ana", 35)
print(e.get_salary())          # prints 0
e.set_salary(1000)
print(e.get_salary())          # prints 1000
e.salary_change(2000)
print(e.get_salary())          # prints 3000
e.salary_change(-50000)
print(e.get_salary())          # prints 0
print(e.has_friends())         # prints False
e.add_friend("bob")
print(e.has_friends())         # prints True
print(e.past_salaries_list())  # prints [0, 1000, 3000, 0]
print(e.past_salary_freq())    # prints {0: 2, 1000: 1, 3000: 1}



# The second finger exercise of lec 19

class Container(object):
    """
    A container object is a list and can store elements of any type
    """
    def __init__(self):
        """
        Initializes an empty list
        """
        self.myList = []

    def size(self):
        """
        Returns the length of the container list
        """
        return len(self.myList)



    def add(self, elem):
        """
        Adds the elem to one end of the container list, keeping the end
        you add to consistent. Does not return anything
        """
        self.myList.append(elem)


class Stack(Container):
    """
    A subclass of Container. Has an additional method to remove elements.
    """
    def remove(self):
        """
        The newest element in the container list is removed
        Returns the element removed or None if the queue contains no elements
        """
        if len(self.myList) == 0:
            return None
        else:
            self.myList.pop()

# --------------------------------------------------
# Test Case 1: Initial state & removing from empty stack
# --------------------------------------------------
s = Stack()
print("Test 1: Empty stack")
print("Size (expected 0):", s.size())
print("Remove from empty (expected None):", s.remove())
print()

# --------------------------------------------------
# Test Case 2: Adding and removing a single element
# --------------------------------------------------
print("Test 2: Single element")
s.add(42)
print("Size after adding 1 item (expected 1):", s.size())
print("Removed item (expected 42):", s.remove())
print("Size after removal (expected 0):", s.size())
print("Remove again (expected None):", s.remove())
print()

# --------------------------------------------------
# Test Case 3: LIFO order (Last-In, First-Out)
# Newest elements should be removed first.
# --------------------------------------------------
print("Test 3: LIFO order check")
s.add("first")
s.add("second")
s.add("third")

print("Size (expected 3):", s.size())
print("1st remove (expected 'third'):", s.remove())
print("2nd remove (expected 'second'):", s.remove())
print("3rd remove (expected 'first'):", s.remove())
print("4th remove (expected None):", s.remove())
print()

# --------------------------------------------------
# Test Case 4: Interleaved add and remove calls
# --------------------------------------------------
print("Test 4: Interleaved operations")
s.add(1)
s.add(2)
print("Removed (expected 2):", s.remove())

s.add(3)
print("Removed (expected 3):", s.remove())
print("Removed (expected 1):", s.remove())
print("Removed (expected None):", s.remove())
print()

# --------------------------------------------------
# Test Case 5: Heterogeneous element types
# --------------------------------------------------
print("Test 5: Multiple data types")
s.add(100)
s.add([1, 2, 3])
s.add({"key": "value"})

print("Removed dict (expected {'key': 'value'}):", s.remove())
print("Removed list (expected [1, 2, 3]):", s.remove())
print("Removed int (expected 100):", s.remove())
print("Final size (expected 0):", s.size())