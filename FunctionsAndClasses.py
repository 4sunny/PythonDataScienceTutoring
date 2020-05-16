def myAddFunction(int1, int2):
    return int1 + int2


print(myAddFunction(1, 2))

myNum = 23
yourNum = 35

ourTotalAges = myAddFunction(myNum, yourNum)

print(ourTotalAges)

#void functions

def myVoidFunction(mytext):
    print(mytext)




# Showcasing basic class without focus on OOP

class myClass:
    def Add(int1, int2):
        return int1 + int2

    def Sub(int1, int2):
        return int1 - int2

myTotal = myClass.Add(1,2)

myDifference = myClass.Sub(3,1)


print(myTotal)
print(myDifference)


class myObjectCar:
    def __init__(self, model, length, width, color="blue"):
        self.model = model
        self.length = length
        self.width = width
        self.color = color

    def getArea(self):
        return self.width * self.length

    def getVolume(self, height):
        return self.width * self.length * height

class myObjectMatrix:
    def __init__(self, model, length, width, color='blue'):
        self.model = model
        self.length = length
        self.width = width

    def getArea(self):
        return self.model * self.length

    def volume(self):
        return self.length * self.width

    def getOof(self):
        return self.model * self.width



class myMatrix:
    def __init__(self, row1, row2):
        self.row1 = row1
        self.row2 = row2

    def print(self):
        print(self.row1)
        print(self.row2)


rowA = [1,2,3,4,5]
rowB = [2,3,4,5,6]

m = myMatrix(rowA,rowB)

m.print()



