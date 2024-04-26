
# Open a file on the server and read it:

# Example 1

# Hello, and welcome to the read file in Python.

f = open('readfile.txt', 'r')
print(f.read())

# Output: 


# Example 2

# if file located in a different directory

f = open('C:/Users/yourname/Downloads/readfile.txt', 'r')
print(f.read())

# Output:

# Read Only Parts of the File

# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

f = open('readfile.txt', 'r')
print(f.read(5))

# Output: Hello

# Read Lines

# You can return one line by using the readline() method:

f = open('readfile.txt', 'r')

print(f.readline())

# Output: Hello, and welcome to the read file in Python.

# By calling readline() two times, you can read the two first lines:

f = open('readfile.txt', 'r')

print(f.readline())
print(f.readline())

# Output: Hello, and welcome to the read file in Python.

# This is the second line.

f = open('readfile.txt', 'r')

for x in f:
  print(x)
  
# Output: Hello, and welcome to the read file in Python.
# This is the second line.

# Close Files

# It is a good practice to always close the file when you are done with it.

f = open('readfile.txt', 'r')
print(f.readline())
f.close()

