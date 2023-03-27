filename = "foo"
try:
    f = open(filename)
except FileNotFoundError:
    errmsg = filename + " not found"
except (TypeError, ValueError):
    errmsg = "invalid filename"

if errmsg != "":
    exit(errmsg)
