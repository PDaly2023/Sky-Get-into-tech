#!/usr/bin/python

# Example Python script

import sys

argc = len(sys.argv)

if argc > 1:
    print('Too many args')
else:
    where = 'World'
    print("Hello", where)

print('Goodby from ' + sys.argv[0])
