import random
from math import prod
import operator as op

print('\nExercise 1a\n')
listOfNumbers = [1, 2, 3, 5, 6, 7, 8, 9, 10]
numbers = set(listOfNumbers)
newList = []
for i in range(1, listOfNumbers[-1]):
    if i not in numbers:
        newList.append(i)
print(newList)

print('\nExercise 1b\n')
listOfNumbers.pop(random.randrange(len(listOfNumbers)))
print(listOfNumbers)

print('\nExercise 1c\n')
list2 = []
for i in range(1,101):
    list2.append(i)

randNum = random.randint(1,100)
random_removal = random.choices(list2, k=randNum)

print(list2)
print('There were:',len(random_removal),' numbers removed')
print(random_removal)

print('\nExercise 1d\n')
print(listOfNumbers)
random_duplicate = random.choice(listOfNumbers)
listOfNumbers.append(random_duplicate)
print(random_duplicate)
print(listOfNumbers)

print('\nExercise 2a\n')
my_tuple = 2, 5, 12, 7 ,9
# my_list = list(my_tuple)
# my_list.sort()
# difference = my_list[-1] - my_list[0]
# print(difference)
difference = max(my_tuple) - min(my_tuple)
print('the difference is', difference)

print('\nExercise 2b\n')
#import .prod from math and use that :) could use variables to store numbers in positions and multipy individually
print(prod(my_tuple))


print('\nExercise 2c\n') #tuple is immutable, so lets create it using a list then convert to a tuple, could make lots of tuples and concatenatre to new tuple?
new_tuple = ()
new_list = []
random_length = random.randint(1,5)

for i in range(random_length):
    new_list.append(random.randrange(1,50))
new_tuple = tuple(new_list)
print(new_tuple)



print('\nExercise 3a\n')

myDictionary = {'Becci': 'Green', 'Steve': 'orange', 'Melinda': 'Purple', 'Ryan': 'Orange', 'Nate': 'Green', 'Anna': 'Green'}
print(myDictionary)

print('\nExercise 3b\n')

myDictionary['Phil'] = 'Red'

print(myDictionary)

print('\nExercise 3c\n')
print(list(myDictionary.values()))
new_dict = list(myDictionary.values())
count = 0
for i in new_dict:
    count = count + new_dict.count(i)
