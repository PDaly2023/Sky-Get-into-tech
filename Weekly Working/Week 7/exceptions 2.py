import sys
try:
    f = open("foo")
except FileNotFoundError as err:
    print("could not open", err.filename, err.args[1],
          file = sys.stderr)
    print("Exception arguements:", err.args, file=sys.stderr)