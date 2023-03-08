# Functions are Objects
# Defined with def statement, followed by arguements list
# just like ocnditionals, membership is by indentation

def make_list(val, times):
    res = str(val) * times
    return res

# arguemsnts are named
# Defaults may be assigned
# return statement is optional
# Any object type may be returned
# Default is the empty object None
# scope
# Variables are local if assigned
# Unless the keyword global is used
# Function names should be lowercase... -PEP008 (standard formatting python enhancement proposal)

# Values required be the function
# Specified withtin the parenthese of the function declaration
def print_list(val, times):
    print (str(val) * times)


# Assigning default values to parameters
# Assign the default value when defining the function
# Need to pass the parameter value while calling it

#once you start adding a default. anything after it has to have a default!!!!
def print_vat(gross, vatpc=17.5, message='summary:'):
    net = gross/(1 + (vatpc/100))
    vat = gross - net
    print(message, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net,vat))

print_vat(9.55)

print_vat(9.55, message='final sum:')

# passing parameters

# BY POSITION
# def my_func (file, blah, date)
# my_func('one', 'two', 'three')
# BY DEFAULT
# my_func('one', 'two', 'three')
# BY NAME
# my_func(blah = 'one', file = 'two', date = 'three')

# use a bare * to force a user to supply named arguements
# def print(vat(*, gross=0, vatpc=17.5, message='Summary:'):

# Attempting to pass positional parameters will fail!!!
# print_vat(15, 9.55) Will fail

#can unpack a tuple to the arguements

#def my_fucntion(a,b,c,):
#   print(a,b,c)

# my_tup = 1,2,3
# my_func(*my_tup)


#variadic arguements - packing and unpacking

# will unpack tuple and make the 3 arguements what was in the tuple

# can do the opposite to pack things into a tuple

#def my_func(dir, *files):
#    print('dir:', dir, 'files:', files)

#chris example
def test_function(*y):
     print(y)

test_function(2, 1.5, 4, 5)

def test_function2(x, y, z, four):
    print(x, y, z, four)

my_tuple = 2, 1.5, 4, 5
test_function2(*my_tuple)

# KEYWORD PARAMETERS
# look like the key-value pairs of a dictionary
# because that is what they are
# Prefix with ** to indicate a dictionary
# since a dictionary is unsorted, so are teh parameters
# may only come at the end of a parameter list
def print_vat(**kwargs):
    print(kwargs)
print_vat(vatpc=15, gross=9.55, message='Summary')

#chris example

def my_func3(**my_arguement):
    print(my_arguement)

my_func3(one='fun', two='python')

def my_func3(x, y, z):
    print(x, y, z)

my_dict = {'x':15, 'y':20, 'z':25}
my_func3(**my_dict)

#Returning objects from a function
# use return statement, followed by the object to be returned
# any object can be returned
# returning an object:
# ends execution of that function
# anything after return is unreachable - unless in a conditional. unless condition is met
