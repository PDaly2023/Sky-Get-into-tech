from account import Account
# capital detones a class
# calls a class from within a module

some_account = Account(1000.00)
some_account.deposit(550.23)
some_account.deposit(100)
some_account.withdraw(50)
print(some_account.getbalance())

another = Account(0)

print (Account.numCreated)

#memory address of object
print("object another is a class", another)
#name of class and package/module
print("object another is a class", another.__class__)
#how to find the name of the class used
print("object another is a class", another.__class__.__name__)