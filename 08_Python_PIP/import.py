# Frist install camelcase module using pip
# pip install camelcase
# uninstall camelcase module using pip
# pip uninstall camelcase



# To list pip packages, you can use the pip list command.
# pip list

# import camelcase module

# To list all the files in the current directory, you can use the os.listdir() method.
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt)) # Hello World