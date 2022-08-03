#This while loop will print "Hello World!" five times
def SimpleWhileLoop():
    spam = 0
    #The while loop while continually check if spam is less than 5.
    while spam < 5:
        print("Hello World!")
        spam = spam + 1

def ComplictatedWhileLoop():
    CorrectName = "Luis"
    Name = ""
    #The while loop will check if user input is equal to the CorrectName variable
    while Name != CorrectName:
        print("Please type the correct name.")
        Name = input()
    #This ending statement, or outro, uses formatting to implement variables.
    print("Thank you {0}! You are {age} years old today.".format(Name, age = 33))

def WeirdWhileLoop():
    Name = ""
    while True:
        print("Please type your name")
        Name = input()
        #Break function will stop while loop and allow the outro to be made
        if Name == "Luis":
            break
    print("Thank you {0}! You are {age} years old today.".format(Name, age = 33))

print("Decide which while loop. simple or complicated")
UserInput = input()

if UserInput == "simple" or UserInput == "sim":
    SimpleWhileLoop()
elif UserInput == "complicated" or UserInput == "com":
    ComplictatedWhileLoop()
elif UserInput == "weird" or UserInput == "we":
    WeirdWhileLoop()