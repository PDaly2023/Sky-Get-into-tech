speed = 40
distance = 35
name = "bob"

if name == "bob":
    if distance > 30:
        if speed < 50:
            print("all as it should be")


if name == "bob" and distance > 30 and speed < 50:
    print("all as it should be 2")


if name == "bob" and not distance > 40 and not speed < 30:
    print("all as it should be 3")

if speed < 30:
    print("lower")
elif speed == 50:
    print("equals")
else:
    print("all as it should be 4")


#can use ALL in a list to see if ALL are true


#exceptions
#x = 10
#if x > 5:
#    #raise an exception
#    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

#assert
import sys

#would tun fine on linux. using assert to catch windows
assert ('linux' in sys.platform), "This code runs on Linux only."

