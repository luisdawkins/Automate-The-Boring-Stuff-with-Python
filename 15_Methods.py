spam = ['hello','hi','howdy','heyas']

def ListSentence():
    for i in range(4):
        print( "The word {} is this place in the list {}.".format(spam[i],int(spam.index(spam[i])) ) )
        print()

#How to return numerical placement of value in list
print(int(spam.index('hello')))

print("This is the beginning list.")
print(spam)
print()

print("This will add 'moose' at the end of the method.")
spam.append('moose')
print(spam)
print()

print("This will place the value 'Cow' in the second spot of the list.")
spam.insert(1, 'Cow')
print(spam)
print()

print("This will remove the 'Cow' value.")
spam.remove('Cow')
#This will also remove a list value, in this case 'Cow'.
#del spam[0]
print(spam)
print()

print("This will sort your list in order. In this case, alphabetical order.")
spam.sort()
print(spam)
print()

print("This will sort your list in reverse order. In this case, reverse alphabetical order.")
spam.sort(reverse=True)
print(spam)
print()

print("The sorting order is called 'ASC11-betical' order, which sorts in uppercase letters first.")
print("To truly sort a list by alphabetical order sort using this function, 'spam.sort(key=str.lower).")