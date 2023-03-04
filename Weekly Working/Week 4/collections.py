myTuple = ('1','2','3','4','5','6')
print(myTuple)
myTuple2 = ('first', 'second', 'third','fourth','fifth','sixth')

for count in range(len(myTuple)):
    print(f'the {myTuple2[count]} number in my tuple is: {myTuple[count]}')

print('\n')

#chris's example sing enumerate
for i, label in enumerate(myTuple2):
    print(f'The {label} Number is {i +1}')