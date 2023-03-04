myList = ['apple', 'orange', 'pear']

#start at 1, end at 10, step by 2)


for i in range(len(myList)):
    print(myList[i])

#item isn't a thing in the list. just making new var called item and printing it
for item in myList:
    print(item)

#replace items in list with sponge string
for index, value in enumerate(myList):
    myList[index] = "sponge"
    print(myList)

#how to exit a script
"""

good practice is to import the sys module

os._exit (integer_expression)
cannot be trapped
returns integer_expression to the caller (usually the shell)

os.abort()
raises a sigbrt signal (trapple in unix)
causes a core dump on unix an exit3 on windows

sys.exit (expression)
rasises a systemexit exception which can be trapped
reaturns expression to the caller (usually the shell) if it is an interger
prints to stderr if any other type of object
    returns1 to the caller
    
sys.exit("Goodbye") - this is what is returned if you do it this way

BASICALLY terminate a process using sys.exit()

