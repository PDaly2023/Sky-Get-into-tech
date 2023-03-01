
import getpass

PIN = "1234"
# PIN set as a string due to getpass.getpass only accepting string as input

attempts = 0
max_attempts = 3
# variables for number of attempts and maximum amount of attempts set
# second version of code only runs down from max amounts of attempts

while attempts < max_attempts:
    # run loops as long as there are attempts left

    supplied_pin = getpass.getpass(prompt='Enter your PIN: ')
    # request user to input pin, getpass will not echo any input

    if supplied_pin == PIN:
        print("You're in!")
        break
        # If entered pin is correct, break out of loop

    if attempts < max_attempts:
        attempts += 1
        print("Wrong PIN!")
        # if wrong pin but not reached max attempts, add 1 to number of attempts and print "Wrong PIN!"

        if attempts == 3:
            print("Your account has been locked.")
            # if we have reached 3 failed attempts, will lock account

        else:
            print(f"You have {max_attempts-attempts} attempts left.")
            # if not at failed 3 attempt, print remaining attempts


# PIN = "1234"
# attempts = 3
#
# while attempts > 0:
#     supplied_pin = (input("Enter your PIN: "))
#     if supplied_pin == PIN:
#         print("You're in!")
#         break
#     else:
#         print("Wrong PIN!")
#         attempts -= 1
#         if attempts == 0:
#             print("Your account has been blocked.")
#         else:
#             print(f"Incorrect PIN. You have {attempts} attempts left.")
