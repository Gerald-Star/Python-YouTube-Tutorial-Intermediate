

# What is Python Lambda?

# A lambda function is a small anonymous function.

# A lambda function can take any number of arguments, but can only have one expression.

# Syntax

# lambda arguments : expression

# The expression is executed and the result is returned:

# Example

# A lambda function that adds 10 to the number passed in as an argument, and print the result:

x = lambda a : a + 10

print(x(5)) # 15

# Lambda functions can take any number of arguments:

# Example

# A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b : a * b

print(x(5, 6)) # 30

# Example

# A lambda function that sums argument a, b, and c and print the result:

x = lambda a, b, c : a + b + c

print(x(5, 6, 2)) # 13

# Why Use Lambda Functions?

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Say you have a function definition that takes one argument, 
# and that argument will be multiplied with an unknown number:

# Example

def myFunc(n):
  
  return lambda a : a * n

myDoubler = myFunc(2)

print(myDoubler(11)) # 22

# Or, use the same function definition to make a function that always triples the number you send in:

# Example

def myFunc(n):
  
  return lambda a : a * n

myTripler = myFunc(3)

print(myTripler(11)) # 33

# Or, use the same function definition to make a function that always multiply the number you send in with 4:

# Example

def myFunc(n):
    
    return lambda a : a * n
  
myQuadrupler = myFunc(4)

print(myQuadrupler(11)) # 44

# Use lambda functions when an anonymous function is required for a short period of time.

# Path: 06_Python_Lambda/Lambda.py

# Use same function to make both functions, in the same program

def myFunc(n):
  
  return lambda a : a * n

myDoubler = myFunc(2)

print(myDoubler(11)) # 22

myTripler = myFunc(3)

print(myTripler(11)) # 33

myQuadrupler = myFunc(4)

print(myQuadrupler(11)) # 44