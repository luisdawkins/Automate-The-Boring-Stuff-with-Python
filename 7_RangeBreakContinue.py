def JimmyOld():
    print("My name is")
    for i in range(0, 5):
        print('Jimmy Five Times ' + str(i))

def JimmyNew():
    print("My name is")
    i = 0
    while i < 5:
        print('Jimmy Five Times ' + str(i))
        i = i + 1

def Total():
    total = 0
    for num in range(101):
        total = total + 1
    print(total)

Total()

print("Old Jimmy function.")
JimmyOld()

print()

print("New Jimmy function.")
JimmyNew()