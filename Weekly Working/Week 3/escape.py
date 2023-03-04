from collections import defaultdict

print("""   this isn't
        very easy\u00A1 \u2191""")

print("\N{Inverted Exclamation Mark}")

string = 'hello'

if 'o' in string:
    print("hurrah")

#write some code to count thenumber of letter f's in this sentence'

sentence = "Finished files are the result of years of scientific study combined with the experience of years."

#chain methods together
print(sentence.lower().count('f'))
#using default dictionary will create a dictionary with the items rather than throw a wobby that it does not exist
chars = defaultdict(int)

for char in sentence:
    chars[char] += 1

print(chars)


#string.format
"Hello Steve I owe you $123.0991"
name = "Steve"
owed = 123.0991
print('Hello ', name, "I owe you $", owed)
#OR {0} name = first arg, {1} owed = second arg with additional formatting arguements d= integer f = float
print("Hello {0}, I owe you ${1: 9.2f}".format(name, owed) )
# add _> to add _ up to 9 digits
print("Hello {0}, I owe you ${1:_>9.2f}".format(name, owed) )

