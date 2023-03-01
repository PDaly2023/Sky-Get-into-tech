mytuple = 'eggs', 'bacon', 'spam', 'tea'
#x,y,z = mytuple
#value error: too many values to unpack

x,y,*z = mytuple
print(x,y,z)
#grabs any others beyond y into one list

t1 = 'cat','dog','python','mouse','camel'
t2 = 'kelp','crab','lobster','fish'

for a, *b, c in t1, t2:
    print(a,b,c)

# * at b means a and c grab first and end and all extras make a list around b
#can only use one * as it will not make sense and throw an exception




