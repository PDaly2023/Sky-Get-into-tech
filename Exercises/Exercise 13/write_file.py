#write a line of code to create a file handle to open and append to a file called pelican.txt

fileObject = open('pelican.txt',mode='a+')
text = 'A wonderful bird is the pelican\n'
text2 = 'His bill holds more than his belican\n'
lines = ["He can take in this beak, \n", "Enough food for a week, \n", "But I'm damned if I can see how the helican. \n"]
fileObject.write(text)
fileObject.write(text2)
for i in lines:
    fileObject.write(i)
fileObject.close()

# \n is required to add a line break so that each new part is added as a new line rather than one continuous line