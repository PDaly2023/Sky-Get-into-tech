import sys

argc = len(sys.argv)

if argc  > 1:
    print("too many args")
else:
    where = "world"
    print ("hello", where)

print ("Goodbye from " + sys.argv [0])
