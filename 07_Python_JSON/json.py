
import json

# Python JSON

# JSON is a syntax for storing and exchanging data.

# JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be used to work with JSON data.

# Parse JSON - Convert from JSON to Python

# If you have a JSON string, you can parse it by using the json.loads() method.



# some JSON:

# x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
#y = json.loads(x)

# the result is a Python dictionary:

#print(y["age"]) # 30


# Convert from Python to JSON

# If you have a Python object, you 
# can convert it into a JSON string by using the json.dumps() method.

# a Python object (dict):

x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:

y = json.dumps(x)

# the result is a JSON string:

print(y) # {"name": "John", "age": 30, "city": "New York"}


# Example of converting Python objects into JSON strings:

print(json.dumps({"name": "John", "age": 30})) # {"name": "John", "age": 30}

print(json.dumps(["apple", "bananas"])) # ["apple", "bananas"]

print(json.dumps(("apple", "bananas"))) # ["apple", "bananas"]

print(json.dumps("hello")) # "hello"

print(json.dumps(42)) # 42

print(json.dumps(31.76)) # 31.76


# Convert a Python object containing all the legal data types:
"""

Python  JSON
dict    Object

list    Array

tuple   Array

str     String

int     Number

float   Number

True    true

False   false

None    null


"""

# Example

print(json.dumps({"name": "John", "age": 30, "city": "New York"})) 
# {"name": "John", "age": 30, "city": "New York"}

print(json.dumps(["apple", "bananas"])) 
# ["apple", "bananas"]

print(json.dumps(("apple", "bananas"))) 
# ["apple", "bananas"]

print(json.dumps("hello")) # "hello"


w = {
  "name": "John",
  "age": 30,
  "country": "United States of America",
  "cities": ("New York", "California", "Texas"),
  "cars": [
    
    {"model": "BMW 230", "mg": 27.4},
    {"model": "Ford Edge", "mg": 24.1}
    
    ]
}

# convert into JSON:

z = json.dumps(w)

print(z)


