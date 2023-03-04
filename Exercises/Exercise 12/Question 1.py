#question12
cheese = ['cheddar', 'stilton', 'cornish Yarg']
cheese += 'Oke'
print (cheese)

#could have [] around it
cheese = ['cheddar', 'stilton', 'cornish Yarg']
cheese += ['Oke']
print (cheese)

#could have used .append() only takes one arguement so only one item at a time
cheese = ['cheddar', 'stilton', 'cornish Yarg']
cheese.append('Oke')
print (cheese)

#could have used the insert method (number indicates index position)
cheese = ['cheddar', 'stilton', 'cornish Yarg']
cheese.insert(3, "oke")
print(cheese)

#add multiple items to existing list
cheese = ['cheddar', 'stilton', 'cornish Yarg']
cheese += ['Oke','Red leicester']
print (cheese)

#or use extend
cheese = ['cheddar', 'stilton', 'cornish Yarg']
cheese.extend(['Oke','Red leicester'])
print (cheese)
#can use .extend() method to add contents of an existing list/tuple to another list by variable name also