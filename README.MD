# counter
small utility class to count programming language formats in your project files

# example usage
```py
from counterPy import count

counter = count.Counter("./src") # specify the folder you want to count files from

counter.count(count.Methods.PRINT) # print the result
# or...
print( counter.count(count.Methods.RETURN) ) # print the returned result
```
# installation
just clone repo in ur folder fr
