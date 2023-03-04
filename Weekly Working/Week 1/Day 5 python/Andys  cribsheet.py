a = "c"
b = "B"
a = a.upper()
print (a.upper())
print (b.lower())
if a.isupper():
    print ("upper")
    
testword = "hello"
print(testword.count("l"))
      
first = "hello"
second = "world"

print("Hello World")
print(first, second)
print("Hello",second)
print(first,"World")


'''concatonating with + doesnn't include a space.  a comma does'''


#fstrings suck! really important though
print(f"The first word is {first} "
      f"the {second} is ")


#literal print
print("""
 ____________________________________________________
T ================================================= |T
| ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|[L
| __________________________________________________[|
|I __==___________  ___________     .  ,. _ .   __  T|
||[_j  L_I_I_I_I_j  L_I_I_I_I_j    /|/V||(g/|   ==  l|
lI _______________________________  _____  _________I]
 |[__I_I_I_I_I_I_I_I_I_I_I_I_I_I_] [__I__] [_I_I_I_]|
 |[___I_I_I_I_I_I_I_I_I_I_I_I_L  I   ___   [_I_I_I_]|
 |[__I_I_I_I_I_I_I_I_I_I_I_I_I_L_I __I_]_  [_I_I_T ||
 |[___I_I_I_I_I_I_I_I_I_I_I_I____] [_I_I_] [___I_I_j|
 | [__I__I_________________I__L_]                   |
 |                                                  |  -Row
 l__________________________________________________j """)

num = 1
newnum = num + 6
print(newnum)

mystr = "hello"
newstr = mystr + " world"
print(newstr)

print(2 **3)

print(True and True)
print(True and False) #not both are true
print(1 and 1)
print(1 and 0) #1 = True 0 = False

print(1 and 1 and 1 and 1 and 1 and 0) # = 0 as not all are true (1)

#Boolean OR

print(True or False) #as at least one of these is true, will return 1 as either can be true
print(False or True)
print(1 or 0)
print(0 or 0)
print(0 or 0 or 0 or 0 or 0 or 0 or 0 or 1)

print((True or False) and True) #one is True of the true and false AND other is True)

#Boolean NOT
#Must not be true
print(not False) #reverses the input
#i.e 5 is NOT 3. NOT True

name =""
if not name:
    print(name)

mylist2 = ("dave,mike,phil") #create a var with a tuple, convert to a list
mylist = list(mylist2)



#dictionarys

cities = {
    'UK':'London',
    'France':'Paris',
    'Germany':'Hamburg'
}

print(cities['UK'])

#or could do this
cities2 = {
    'UK':['London','Lillies','Nantes'],
    'France':['Paris','lille','Nantes']
}
print(cities2['UK'])

#myset = {2,5,6,7,8,2,5}
#print (myset)

foods = ['cheese', 'bread', 'milk', 'sausage']
print(foods[1]) # first item in list
print(foods[-1]) #last index in list
print(foods[3][0]) #first letter of third index
foods[2] = "yoghurt"
print(foods)

print(foods.pop()) # .pop always takes the last of the list and returns what it stole

print(hex(id(foods))) #prove mutable. can be changed. reference does not change

foods.append('Milkshake') #add to the food list (after sausage has been removed)
print(foods)
print(hex(id(foods))) #prove mutable. can be changed. reference does not change

mytup3 = ("one","two")
print(mytup3[1])

def test(number):
    try:
        number
        number = int(number)
        float(number)
        double = number * 2
        print("Your number times 2 is ", double)  # will output the number twice (i.e. 33 will be 3333)
    except:
        print("not a number")

running = True
while running:
    mynum = (input("Enter a number"))
    test(mynum)

