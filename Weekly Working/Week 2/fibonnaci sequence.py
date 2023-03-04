#The sequence follows the rule that each number is equal to the sum of the preceding two numbers.

#The Fibonacci sequence begins with the following 14 integers:

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 ...

number = 0
number2 = 1
result = 0

exit = False

while exit == False:
    print(result)
    result = number + number2
    number = number2
    number2 = result
    if result > 100:
        break
