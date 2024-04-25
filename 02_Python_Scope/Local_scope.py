
# Local Scope

# A variable is only available from inside the region it is created. This is called scope.

# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

# Example

def myFunc():
  x = 100
  print(x)
  
myFunc() # means calling the function
# print(x) # This will throw an error because x is not available outside the function
# print(myFunc()) # This will throw an error because myFunc() is not available outside the function

print()

# Another Example of local scope in a list of function

def myFunc():
  x = 10
  print(x)
  
myFunc() # 10


print()
#? Example 2
#? Function Inside Function

def myFunc():
  x = 300
  def myInnerFunc():
    print(x)
  myInnerFunc() # 300
  
myFunc()
#! This function will throw an error
#! print(x)
#! print(myInnerFunc())


#? As explained in the example above, the variable x is not available outside the function, but it is available for any function inside the function.

# Example
print()

def myFunc_():
  
  y = 400
  
  def myInnerFunc_():
    print(y)
    
  myInnerFunc_() # 400
  
myFunc_() # 400


print()


   

