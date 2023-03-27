import sys
def my_func():
    try:
        f = open("foo")
    finally:
        print("finally block", file =sys.stderr)

try:
    my_func()
except OSError:
    print("An OS error occurred", file=sys.stderr)