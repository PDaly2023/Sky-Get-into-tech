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

