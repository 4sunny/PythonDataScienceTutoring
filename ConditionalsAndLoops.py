isOn = True

if isOn == True:
    print("It's On")
else:
    print("It's Off")

myInt = 10
if myInt == 20:
    print("Smaller Than 20")

elif myInt == 20:
    print("Same!")

else:
    print("Bigger than 20!")


if "Jimmy" in members:
    print("Jimmy is a member!")
else:
    print("Jimmy is not a member!")


if "Jimmy" in members or "John" in members:
    print("At least one of them is a member")

elif "Jimmy" in members and "John" in members:
    print('They are both members')

else:
    print('None are members')


counter = 10
while counter > 0:
    print(counter)
    counter -= 1

# for {Variable} in {iterator}
members = ["Jimmy", "Jake", "John", "Jack"]
for currentMember in members:
    print(currentMember)

for currentValue in range(10):
    print(currentValue)

myString = "Hello"
for currentCharacter in myString:
    print(currentCharacter)


for index in range(len(members)):
    print(members[index])