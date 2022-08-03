spam = 42 #global variable

def eggs():
    #This will allow the function to manipulate the data of the global spam variable
    global spam
    spam = 44 #local variable

print("Some code here.")
print("Some more code.")
