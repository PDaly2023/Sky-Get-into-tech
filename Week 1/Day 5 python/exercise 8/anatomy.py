# Example Python Script

#import sys module
import sys

argc = len(sys.argv) # declare argc variable. call built in len() function to check length of function

#use selection
if argc > 1: # if argc length is greater than 1
    print("Too many args") # use print() to tell user too many arguements.
else: # otherwise
    where = "world" #declare where variable with string of 'world'
    print("Hello", where) #use print() to display a string then the where variable (value of it - string 'world')
print("Goodbye from " + sys.argv[0]) #use print funtion to display Goodbye from and concatenate the value of sys.argv at index 0
#space required due to concatenate.