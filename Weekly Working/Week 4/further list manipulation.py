#adding items to a list

#on the left
cheese = []
cheese[:0] = ['cheshire', 'Ilchester'] #using a number in squarebracket ina list like this is called slicing
#on the right
cheese += ['oke','Devon blue']
cheese.extend(['oke','Devon blue']) #needs to be in square brackets. if you do it as a string '('oke') it will do O, k, e as elements. strings are sequences

#append can only be used for one item
cheese.append('oke')

print(cheese)

#anywhere

cheese.insert(2, 'cornish brie') #at index 2 insert this item

print(cheese)

#using pop(index)
#returns the deleted item
#del removes the element by name
#remove - removes teh left most item matching teh value
#raises an exception is the item is not found
cheese.remove('oke')

print(cheese)