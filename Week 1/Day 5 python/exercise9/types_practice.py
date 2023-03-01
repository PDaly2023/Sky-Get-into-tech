first = "Phil" #declare 'first variable' with string of Phil
second = "Daly" #decalre second variable with string of Daly

print(first, second) #call print() function pass the two variables to it

nameList = [] #declare an empty list

nameList.append(first) #use append method to add 'first' variable to end of the  list
nameList.append(second) #use append method to add 'second' variable to end of the list
print(nameList) #use print function to display contents of the list

nameDict = {}

nameDict["first"] = first #add 'first' key with value of first var
nameDict["second"] = second # add 'second' key with value of second var
print(nameDict) #use print function to display contents of dictionary. use [] to display individual indexes

