name = "Alice"
password = "swordfish"
age = 3000

#If the name variable is equal to "Alice" then the if statement will return True
if name == "Alice":
    print("Hello " + str(name))
print("Done with name question")

print("")

#password faces two options, True returns "Access granted.", and False returns "Access denied."
if password == "swordfish":
    print("Access granted.")
else:
    print("Access denied.")
print("Done")

print("")

if name == "Sam":
    print("Hello Sam.")
elif age < 12:
    print("You are not Sam, kiddo. You are " + str(age) + " years old.")
elif age > 2000:
    print("Unlike you, Sam is not an undead, " + str(age) + " year old immortal vampire.")
elif age > 100:
    print("You are not Sam, grannie. You are " + str(age) + " years old.")

#In addition to regular boolean statements you will have truthy and falsey value
#For strings some value is True, and nothing is fale
#In constrast, the bool() function will return False for 0, and True for anything else

if bool(0):
    print("It worked")