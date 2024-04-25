

# Positional Arguments in Function

def add(a, b):
    return a + b
  
print(add(10, 20))  # 30

def add(a, b, c):
    return a + b + c
  
print(add(10, 20, 30))  # 60

def add(a, b, c, d):
    return a + b + c + d
  
print(add(10, 20, 30, 40))  # 100

# Keyword Arguments in Function

def add(a, b):
    return a + b
  
print(add(a=10, b=20))  # 30

def add(a, b, c):
    return a + b + c
  
print(add(a=10, b=20, c=30))  # 60

def add(a, b, c, d):
    return a + b + c + d
  
print(add(a=10, b=20, c=30, d=40))  # 100

print()

def myScore(name, score):
    return f"{name} scored {score} runs"
  
print(myScore("Sachin", 70))  # Sachin scored 100 runs

# Keyword Only Argument in Function
def myScore_(*, scores):
  print(scores)
  
myScore_(scores = 100) 

def myScore_(*, score):
  print(score)
  
myScore_(score = 8) 


  """
  This function will throw an error
  def myScore_(*, score):
    print(score)
    
myScore_(8)  

But adding *, / will make it keyword only argument  
  """


print()
# Default Arguments in Function

def add(a, b=0):
    return a + b
  
print(add(10))  # 10

def add(a, b=0, c=0):
    return a + b + c
  
print(add(10))  # 10


# Variable Length Arguments in Function

def add(*args):
    return sum(args)
  
print(add(10, 20, 30))  # 60


# Variable Length Keyword Arguments in Function

def add(**kwargs):
    return sum(kwargs.values())
  
print(add(a=10, b=20, c=30))  # 60


# Path: Function/Functions.py

def add(a, b):
    return a + b
  
print(add(10, 20))  # 30


# 