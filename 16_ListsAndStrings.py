print(list('hello'))

name = 'Zophie'

#slicing and list recalling manipulation
#Lists are mutable, strings are immutable as lists.
print(name[0])

print(name[1:3])

print('Zo' in name)

print('XXX' in name)

for letter in name:
    print(letter)

print()

def ImmutableStings():
    name = 'Zophie a cat'
    print(name)
    newName = name[0:7] + 'the' + name[8:12]
    print(newName)

ImmutableStings()

def eggs(cheese):
    cheese.append('hello')

spam= [1,2,3]
eggs(spam)
print(spam)

#This function will create a copy of a table, then place a value in the copied list.
def CopyOfDataTable():
    import copy

    print()
    spam = ['A','B','C','D','E']
    print(spam)
    cheese = copy.deepcopy(spam)
    cheese[1] = 42
    print(cheese)

CopyOfDataTable()

print()
print("Four score and seven " + \
      "Frick anybody in this establishment.")