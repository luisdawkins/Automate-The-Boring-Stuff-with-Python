#This program says hello, then asks for my name and age

print('Hello World!')

print('What is your name?') # ask for their name
#This variables recieves input from user through command prompt
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
#len function evaluates the number of characters in a string
print(len(myName))

print('What is your age?') # ask for their age
myAge = input()
#str function converts a data type into a string
#This allows variables to be concatenated with text
#int, str, and float all convert valye data types
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

