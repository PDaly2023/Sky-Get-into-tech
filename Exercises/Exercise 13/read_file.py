readFile = open('pelican.txt').read()
print('\nThe file is opened as:', type(readFile),'\n')
print(readFile)

pelicanList = open('pelican.txt').readlines()
print(len(pelicanList),'\n')
print(pelicanList)

print('\nLooping over the contents of the file from list - without blank lines. using strip to remove \\n \n')

for i in pelicanList:
    print(i.strip('\n'))




