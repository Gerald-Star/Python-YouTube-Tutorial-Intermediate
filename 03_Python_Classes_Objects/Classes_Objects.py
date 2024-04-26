
#? What is Python Classes/Objects?


# To create a python class, the 'class' keyword is used.

class MyFirstClass:
    x = 10
    
    print(x)
print(MyFirstClass)  # <class '__main__.MyFirstClass'>
# meaning MyFirstClass is a class in the __main__ module



#? Create an object of the class

class MyFirstClass:
    x = 20
    
    print(x)
    
obj = MyFirstClass()

print(obj)  # <__main__.MyFirstClass object at 0x7f8b1c1b5d30>  


print()
# Another Example

class Person:
    name = "John"
    age = 36
    
    print(name)
    print(age) 
    
class Number:
  x = 50
  
p1 = Number()
print(p1.x)  # 50
      
    


 
# The __init__() Function

# The examples above are classes and objects in their simplest form, and are not really useful in real life applications.

# To understand the meaning of classes we have to understand the built-in __init__() function.

# All classes have a function called __init__(), which is always executed when the class is being initiated.

# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# Example

class Person:
  
  def __init__(self, name_, age_):
    self.name_ = name_
    self.age_ = age_
    
p1 = Person("Smith", 30)

print(p1.name_)  # John

print(p1.age_)  # 36

# Note: The __init__() function is called automatically every time the class is being used to create a new object.



#? Object Methods

# Objects can also contain methods. Methods in objects are functions that belong to the object.

# Let us create a method in the Person class:

# Example

class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myFunc(self):
    print(f"Hello my name is {self.name}")
    
p1 = Person("John", 36)

p1.myFunc()  # Hello my name is John

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.

# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:


#? The_str_() Function

# The __str__() function is called automatically when a new object is created.

# It is used to print a readable version of the object.

# When you try to print an object using the print() function, Python calls the __str__() method of the object.

# Example

class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def __str__(self):
    return (f"Hello my name is {self.name}, and I am {self.age}")
  
p1 = Person("Mercy", 26)

print(p1)  # Hello my name is Mercy


# Modify Objects

# You can modify properties on objects like this:

# Example

class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myFunc(self):
    print(f"Hello my name is {self.name}")
    
p1 = Person("Merry", 36)

p1.age = 20 # this modifies the age of the object

print(p1.age)  # 20  


# Delete Objects

# You can delete objects by using the 'del' keyword:

class Person:
  
  def __init__(self, name, age):
    self.name = name
    self.age = age
    
  def myFunc(self):
    print(f"Hello my name is {self.name}")
    
p1 = Person("Merry", 36)

del p1

# print(p1)  # This will raise an error because the object no longer exists


# The pass Statement

# class definitions

# The pass statement is used as a placeholder for future code.

# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.

# Empty class definition

class Person:
  pass