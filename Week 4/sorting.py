#sort by size - sort can sort any iterable (often a sequence)
cheese = ['cornish yarg', 'oke', 'edam', 'stilton']
cheese.sort(key=len)
print(cheese)

#sorted returns a sorted list - regardless of the original  type
#sort - sorts a list in place

#BOTH have te following optional named paratmeters
#key=sort_key - function which takes a single arguement
#reverse=True - Default is false

nums = ['1001', '34', '3', '77', '42','9', '87']
newstr = sorted(nums)
newnum = sorted(nums,key=int)
print(newstr)
print(newnum)

#sort algorithm is the adaptive stable mergesort (algorithm by Tim peters)

#sort alphabetically
cheese.sort()
print(cheese)
