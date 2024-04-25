

# Global Scope

# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.

# Example
  
x = 500

def myFunc__():
  print(x)  
  
myFunc__() # 500

print(x) # 500


# Naming Variables
# If you operate with the same variable name inside and outside of a function, Python will treat them as two separate variables, one available in the global scope (outside the function) and one available in the local scope (inside the function):

# Example

x = 600

def myFunc___():
  x = 700
  print('Local ID:', x)
  
myFunc___() # 700

print('Global ID:', x) # 600


print()


#? Global Keyword

# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

# Example

def myFunc____():
  global x
  x = 800
  
myFunc____()

print(x) # 800


print()
# Another Example

id = 5

def getID_____():
  id = 10
  print('Local ID:', id)
  
getID_____() # Local ID: 10

print('Global ID:', id) # Global ID: 5

# Also, use the global keyword if you want to make a change to a global variable inside a function.

# Example

x = 900

def myFunc_____():
  
  global x
  x = 1000
  
myFunc_____()

print(x) # 1000


print()
# Example

def myFunc______():
  
  global x
  x = 1100
  
myFunc______() # 1100

print(x) # 1100



# Also, use the global keyword if you want to make a change to a global variable inside a function.

# Example

x = 1200

def myFunc_______():
  
  global x
  x = 1300
  
myFunc_______()

print(x) # 1300


print()

Name = "Sachin"

def myName():
  global Name
  Name = "Rahul"
  
myName()

print(Name) # Rahul

print()

# Example

Name = "Sanjay"

def myName_():
  global Name
  Name = "Roman"
  
myName_()
print(Name) # Roman


# To change the value of a global variable inside a function, 
# refer to the variable by using the global keyword:


# NON-LOCAL KEYWORD VARIABLE

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.

# If you want to modify a variable inside a function, you can use the nonlocal keyword:

# Example - RECHECK

def myNonFunc________():
  
  x = 1200
  
  def myNonInnerFunc________():
    nonlocal x
    x = 1600
    
    myNonInnerFunc________()
    return x
print(x) # 1500  


def  monLocalFunc():
  x = 1500
  def myNonInnerFunc________():
    nonlocal x
    x = 1600
    myNonInnerFunc________()
    return x
  
print(monLocalFunc()) # 1600 