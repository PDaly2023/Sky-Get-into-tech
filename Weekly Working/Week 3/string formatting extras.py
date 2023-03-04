string = 'hello'

print(string.capitalize())             #= Hello
print(string.lower())
print(string.upper())                   #hello//HELLO
print("<", string.center(12)+'>')                   #"       hello       ""
print(string.ljust(12)+'>')                    #"hello"              "
print('<', string.rjust(12))                    #"               hello"
print(string.zfill(12))                   #"***************hello"

#further formatting
#f strings

name = 'Phil'
print(f'My Name is {name}')

names = ['tom', 'Harry', 'Jim', 'Dave']
suffix = ['st', 'nd', 'rd', 'th']
n = 1

#using \ to move text to next line but still be part of this line
s = f'{str(n + 1) + suffix[n]} of \
{len(names)} is {names[n]}'

print(s)

#a python string is an immutable sequence type
text = 'remarkable bird, the Norwegian Blue'
#print only these letters, think of them as index numbers like in a list
print(text[11:14])
print(text[-7:-1])
#if ommitting an arg, it uses the default. i.e. first or last as below
print(text[:14])
print(text[-7:])

