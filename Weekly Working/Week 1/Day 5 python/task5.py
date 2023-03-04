name = input("Please enter your name: ")
# Calculate the number of letters in the name
num_letters = len(name)
# Print the number of letters
print("Your name has", num_letters, "letters.")
# Check if any letters are the same
has_duplicate = False
for i in range(num_letters): #for loop 'i' iterate through string
    for j in range(i + 1, num_letters): #nested for loop 'j' iterate through string  checking each letter against current 'i'
        if name[i] == name[j]: #if i == j, has duplicate = true. exit loop
            has_duplicate = True
            break
    if has_duplicate: # if has duplicate = true exit i loop
        break
# Print the result of the check for duplicate letters
if has_duplicate: # if has duplicate is true after loops have exited
    print("Your name has duplicate letters, the first occurance is: ", name[i]) #print that a duplicate was found, show which letter was found (only finds first instance)
else:
    print("Your name does not have any duplicate letters.") # if no duplicates. print this instead


name = input("enter your name: ")
print(f"the number of letters is {len(name)}")

##Andy's version'
##repeats = set()
##for i in name:
##    if name.count(i) > 1:
##        repeats.add(i)
##print("Repeated Letters")
##for i in repeats:
##    print(i)

