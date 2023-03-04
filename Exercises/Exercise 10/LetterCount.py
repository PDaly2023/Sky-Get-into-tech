letter_check = "e"
s = "Finished files are the result of years of scientific study combined with the experience of years."
s = s.lower()
print(f"\n{s}")
print(f"\nThe letter {letter_check} appears {s.count(letter_check)} times in the above sentence.")


print("\nHere is a breakdown of all letters:")
letter_count = {}

for char in "abcdefghijklmnopqrstuvwxyz":
    letter_count[char] = 0

for char in s:
    if char.isalpha():
        char = char.lower()
        letter_count[char] += 1

print(letter_count)
