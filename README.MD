# counter
small utility class to count files in your folder by file extensions

# example usage
```py
from counterPy import count

counter = count.Counter("./src") # specify the folder you want to count files from

counter.count(count.Methods.PRINT) # print the result
# or...
print( counter.count(count.Methods.RETURN) ) # print the returned result
```
# installation
clone repo in your folder

