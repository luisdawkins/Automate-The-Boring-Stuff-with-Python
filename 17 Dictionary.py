#Dictionary
#The key: value format is "Size": "Fat"
MyCat = {"Size": "Fat", "Color": "Gray", "Disposition": "Loud"}

#Display dictionary data values
def DisplayDictionaryDataValues():
    print()
    print("All data values of the MyCat dictionary")
    print(MyCat)
    print()

DisplayDictionaryDataValues()

#The print command calls upon a key to return the corresponding value
def PrintSelectValue(Key):
    print()
    print(MyCat[Key])
    print()

#PrintSelectValue("Size")

#Concatenation
def PrintSimpleMessage():
    Message = "My cat has " + MyCat["Color"] + " fur."
    print()
    print(Message)
    print()

#PrintSimpleMessage()

#The following commands are dictionary methods
#The dictionary methods display different components of a dictionary
def DictionaryMethods():
    print()
    print("MyCat dictionary keys:")
    print( list(MyCat.keys()) )
    print()
    print("MyCat dictionary values:")
    print( list(MyCat.values()) )
    print()
    print( list(MyCat.items()) )
    print()

#DictionaryMethods()

#Advanced uses of dictionary methods
def AdvancedDictionaryMethods():
    print("Print each key independently:")
    for KeyValue in MyCat.keys():
        print(KeyValue)
    print()
    print("Print each key:value pair independently")
    for KeyValue, Value in MyCat.items():
        print (KeyValue + " : " + Value)
    print()

#AdvancedDictionaryMethods()

#get function is useful when retrieving a dictionary key:value pair and avoiding a key error if none exists
def getDictionary(KeyValue):
    print()
    print(MyCat.get(KeyValue, "'{}' is not a valid key.".format(KeyValue)))
    print()

#getDictionary( str(input()) )

#setdefault is useful when adding a key:value if a key doesn't already exist
def setdefaultDictionaryFunction():
    print()
    print( MyCat.setdefault("Age", "4") )
    print()

setdefaultDictionaryFunction()
