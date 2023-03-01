#task Two

def test(number):
    try:
        number = int(number)
        for i in range(number):
            if i % 2 == 0: #how we find even numbers
                print("the even numbers are", i )

    except:
        print("not a number, try again")


exit = False

while exit == False:
    user_input = input("Enter a whole number between 1 and 100 or s to quit ")
    if user_input == 's':
        exit = True
        print('Thank you for using the my Program')
    else:
        test(user_input)

#decided to use a while loop and function with error checking. made debugging easier than re-running the code each time