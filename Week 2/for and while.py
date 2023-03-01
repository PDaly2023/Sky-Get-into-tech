def test(number):
    try:
        number = int(number)
        for i in range(number):
            if i % 2 != 0: #how we find odd numbers
                print("the odd numbers are", i )

    except:
        print("not a whole number, try again")

number = 0
number2 = 1
result = 0

exit = False

while exit == False:
    user_input = input("Enter a whole number between 1 and 100 or s to quit ")
    if user_input == 's':
       exit = True
       print('Thank you for using the my Program')
    else:
        test(user_input)





