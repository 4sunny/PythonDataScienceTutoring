#https://jupyter.org/try

myInt = 10
# Addition
print(myInt + 1)

# Subtraction
print(myInt - 1)

# Multiplication
print(myInt * 2)

# Division
print(myInt / 2)

myFloat = 0.314
print(myInt + myFloat)


isOn = True
isOff = False


myString = "Hello World!"
print(myString)
# Concatenation
string1 = 'Hello'
string2 = 'World!'
print(string1 + ' ' + string2)
#String slicing
print(myString[0])
print(myString[6:])
print(myString[:6])
print(myString[3:7])
#String functions
print(myString.split())
print(myString.lower())
print(myString.upper())


myList = [1, "2", 3, 4, 5]
print(myList[0])

myList.append(6)
print(myList)

myList.pop(1)
print(myList)

myStrList = ["Jimmy", "Jake", "John", "Jack"]
print(myStrList.index("Jake"))

print(len(myStrList))


myDictionary = {"Christa": 32, "Emily": 21, "Katie": 25, "Maika": 36}

myDictionary["Jane"] = 35
print(myDictionary)

print(myDictionary["Christa"])

print(myDictionary.keys())
print(myDictionary.values())

print(myDictionary.items())

# Also a good idea to learn matrices, tuples and sets