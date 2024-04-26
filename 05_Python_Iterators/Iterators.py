

# Python Iterators

#* __iter__() Method
# The __iter__() method acts similar, you can do operations (initializing etc.), but must always return the iterator object itself.

#* __next__() Method
# The __next__() method also allows you to do operations, and must return the next item in the sequence.


#? Example

# Return an iterator from a tuple, and print each value:

mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple)

print(next(myit))

print(next(myit))

print(next(myit))


myStr = "banana"

myit = iter(myStr)

print(next(myit))

print(next(myit)) # etc


# Looping Through an Iterator

# We can also use a for loop to iterate through an iterable object:

# Example

# Iterate the values of a tuple:

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)
  
# Iterate the characters of a string:

myStr = "banana"

for x in myStr:
  print(x)
  
# Create an Iterator

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# __iter__() method, you can do operations 
# __next__() method, you can also do operations, and must return the next item in the sequence.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    x = self.a
    self.a += 1
    return x
  
myclass = MyNumbers()

myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))


# STOP ITERATION

# The example above would continue forever if you had enough next() statements, or if it was used in a for loop.

# To prevent the iteration to go on forever, we can use the StopIteration statement.

# In the __next__() method, we can add a terminating condition to raise an error if the iteration is done a specified number of times:


class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myClass = MyNumbers()
myiter = iter(myClass)

for x in myiter:
  print(x)

































    
    
    





    
    
    
    
    
    
    
