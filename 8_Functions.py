#This imports a third party modules into my program, allowing me to use already created functions
import random
import sys
import pyperclip

#from random import *, allows you to import a library without specifying a library

#The following code allows me to use the library by calling the library and specific function
Rando = random.randint(1, 10)

print(Rando)

#Functions can take parameters, which hold data
def sysExercise(name):
    print("Hello")
    print("Goodbye, {}.".format(name) )
    sys.exit()


"""
These commands copy a piece of text and pastes the command
import pyper
pyperclip.copy("Hello world!")
pyperclip.paste()
"""

sysExercise("Luis")
ClipPaste()
