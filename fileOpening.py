#Always Close files
myFile = open('SampleTxt.txt','r')
print(myFile)
myFile.close()

myFile = open('SampleTxt.txt','r') # Reading file
myFile = open('SampleTxt.txt','w') # Writes to file
myFile = open('SampleTxt.txt','a') # Appending to file
myFile = open('SampleTxt.txt','x') # Creating file

myImage = open('myImage.png', 'rb') # Reading as binary

with open('SampleTxt.txt', 'r') as myFile:
    print(myFile)
