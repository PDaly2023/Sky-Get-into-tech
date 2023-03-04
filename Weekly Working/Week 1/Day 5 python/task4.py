
mynum = (input("Enter a number "))

try:
    mynum = int(mynum)
    mynum = float(mynum)
    if mynum % 2 == 0: #how we find even numbers
        print("the numbers is even")
    else:
        print("the number is odd")
except:
    print("not a number, try again")