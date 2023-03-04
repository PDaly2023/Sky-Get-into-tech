#exercise 1a
import random

listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
numbers = set(listOfNumbers)
newList = []
for i in range(1, listOfNumbers[-1]):
    if i not in numbers:
        newList.append(i)
print(newList)

#exercise 1b
listOfNumbers.pop(random.randrange(len(listOfNumbers)))
print(listOfNumbers)


#exercise 2a
my_tuple = 2, 5, 12, 7 ,9
# my_list = list(my_tuple)
# my_list.sort()
# difference = my_list[-1] - my_list[0]
# print(difference)
difference = max(my_tuple) - min(my_tuple)
print('the difference is', difference)

#exercise 3a

myDictionary = {'Becci': 'green', 'Steve': 'orange', 'Melinda': 'Purple', 'Ryan': 'Orange', 'Nate': 'Green', 'Anna': 'Green'}

#exercise 3b

myDictionary['Phil'] = 'Red'

print(myDictionary)

