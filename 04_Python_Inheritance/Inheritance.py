
# What is Python Inheritance?

# Inheritance allows us to define a class that inherits all the methods and properties from another class.

# Parent class is the class being inherited from, also called base class.

# Child class is the class that inherits from another class, also called derived class.



#? USE CASES OF INHERITANCE

# It allows us to define a class that inherits all the methods and properties from another class.

# It allows us to reuse code.

# It allows us to create a child class that inherits from a parent class.

# It allows us to create a class that is more specific than the parent class.

# It allows us to create a class that is more general than the parent class.

# It allows us to create a class that is more specialized than the parent class.

# It allows us to create a class that is more generalized than the parent class.

# It allows us to create a class that is more abstract than the parent class.

# It allows us to create a class that is more concrete than the parent class.

# It allows us to create a class that is more detailed than the parent class.

# It allows us to create a class that is more comprehensive than the parent class.

# It allows us to create a class that is more elaborate than the parent class.

# It allows us to create a class that is more intricate than the parent class.

# It allows us to create a class that is more complex than the parent class.

# It allows us to create a class that is more sophisticated than the parent class.

# It allows us to create a class that is more advanced than the parent class.

# It allows us to create a class that is more evolved than the parent class.

# It allows us to create a class that is more developed than the parent class.

# It allows us to create a class that is more mature than the parent class.


# Create a Parent class

# Any class can be a parent class, so the syntax is the same as creating any other class:

# Example

# Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    
  def printname(self):
    print(self.firstname, self.lastname)
    
# Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")

x.printname()

# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Another Example

# Create a class named Student, which will inherit the properties and methods from the Person class:

class Student(Person):
  pass

# Use the Student class to create an object, and then execute the printname method:

x = Student("Mike", "Olsen")

x.printname()

# Add the __init__() Function

# So far we have created a child class that inherits the properties and methods from its parent.

# We want to add the __init__() function to the child class (instead of the pass keyword).

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Example

# Add the __init__() function to the Student class:

class Student(Person):
  def __init__(self, fname, lname):
    # add properties etc.
    pass
  
# When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

# Note: The child's __init__() function overrides the inheritance of the parent's __init__() function.

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

# Example

# Add the __init__() function to the Student class:

class Student(Person):
  
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)
    
# Now we have successfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.

# Use the super() Function

# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:

# Example



class Student(Person):
  
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    
# By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

# Add Properties

# Example

# Add a property called graduationyear to the Student class:
"""
class Student(Person):
  
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = year
    
x = Student("Mike", "Olsen", 2019)  
print(x.graduationyear) # 2019
"""
    
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

# Example

# Add a method called welcome to the Student class:

class Student(Person):
  
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
    
    
# If you add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.

# Example

# Add a method called welcome to the Student class:

class Student(Person):
  
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year
    
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
    
    
# CREATE A CHILD CLASS

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class:

# Example

# Create a class named Student, which will inherit a properties and methods from the Person class:

class Student(Person):
  
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    
# Now the Student class has the same properties and methods as the Person class.

# Use the Student class to create an object, and then execute the printname method:

x = Student("Micheal", "Ondo")


# Add METHOD

# Example

# Add a method called welcome to the Student class:

class Student(Person):
  
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = year
    
  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
    x = Student("Mike", "Olsen", 2019)
    x.welcome()
    
    
    
    
    
    
    

