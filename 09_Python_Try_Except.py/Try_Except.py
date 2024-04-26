
# The Try Except block lets you handle errors, without stopping the script.
# The Except block lets you handle the error.

# The else block lets you execute the code if the try block does not raise any errors.

# The finally block lets you execute the code, regardless of the result of the try- and except blocks.

# Exception Handling

# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

# Example

# The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")
  
  
# Using many exceptions

# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
  
# Using the Else keyword in the Try Except block

# You can use the else keyword to define a block of code to be executed if no errors were raised:

try:#
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")  
  
  
print()  
# Using the Finally keyword in the Try Except block

# The finally block, if specified, will be executed regardless if the try block raises an error or not.

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
print()

# This can be useful to close objects and clean up resources:

# Try to open and write to a file that is not writable:

try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")   
  
  
# Raise an exception

# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.

# Example

# Raise an error and stop the program if x is lower than 0:

x = -1

if x < 0:
  
  raise Exception("Sorry, no numbers below zero")

print()
# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.

# User-defined Exceptions

# You can create your own exceptions by creating a new class.

# This should be a child class of the built-in Exception class.

# Example

# Create a class that will raise an error if the input is a negative number:

class MyError(Exception):
  def __init__(self, value):
    self.value = value
    
  def __str__(self):
    return(repr(self.value))
  
try:
  raise MyError(2)
except MyError as e:
  print("A New Exception occurred: ", e.value)
  
# In the example above, the error is defined in the __init__ method.

# The __str__ method is used to print the error.

# Example

# Create a class that will raise an error if the input is a negative number:

class ValueTooSmallError(Exception):
  def __init__(self, message):
    self.message = message
    
num = 10

try:
  if num < 100:
    raise ValueTooSmallError("The value is too small")
  
except ValueTooSmallError as e:
  
  print(e.message)
  
# The error is defined in the __init__ method.

# The __str__ method is used to print the error.    
  
  
# The raise keyword is used to raise an exception.

# You can define what kind of error to raise, and the text to print to the user.

# User-defined Exceptions

a = 10
b = 0

try:
  c = a/b
  print(c)
except ZeroDivisionError:
  print("Cannot divide by zero")
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
  
# The raise keyword is used to raise an exception.

a = "hello"
if not type(a) is int:
  raise TypeError("Only integers are allowed")

  