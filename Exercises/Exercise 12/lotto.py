import random


number_set = set()

#testing it len)number_set) != 6 is working as intended
#number_set = {1,2,3,4,5,6}
print('I will now draw numbers until i have 6 unique numbers in the range 1-50')

for i in range (100):
    drawn_number = random.randrange(1,50)
    number_set.add(drawn_number)
    print(f'the Number Drawn is.........:{drawn_number}')

    if len(number_set) == 6:
        break
#use * to print set out wihtout {} by unpacking the set
print('The results are in! This weeks Lotto numbers are: ', *number_set)

#originally i went with if len(number_set) != 6.. but then when duplicates occured I would only get 5 or less in the set
#as the loop only iterated 6 times. by setting the possible loop count at a massively higher number, those chances are virtually nil.
#instead I added a condition that detects if the number_set has reached 6 then ends the loop.

#maybe a while len(number_set) !=6 instead