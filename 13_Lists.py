spamList = [["cat", "bat", "rat", "elephant"], [10, 20, 30, 40, 50]]
spamListCount = len(spamList)
print("There are {} items in the array.".format(spamListCount) )

for i in range(spamListCount):
    print(spamList[i])

print()

print("spam list results in the second item in the first part of the array.")
print("spamList[0][1]")
print(spamList[0][1])
print()

print("spam list results in the forth item in the second part of the array.")
print("spamList[1][4]")
print(spamList[1][4])