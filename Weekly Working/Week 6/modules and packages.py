#package is a folder name
#modules are inside of that folder

#modules do not have to be part of a package

#from converse.module import hello
#importing just that function
#when calling the function you can just type hello()

#OR

#from converse import module
#when calling the function you would have to type module.hello()

#to avoid clashes of function names you can use an alias
#from converse.module import hello as module_hello

#from converse.module import *
#import all functions
#could causes clashes as the function names are not known in the code

#__init__ double underscores 'dunders' tells python it's something special - __main__

#when imoprting a module all code (besides functions will run at import)
#by having this code below it detects if it is running inside another __main__ or not
#if it is running by itself, run main()

#def main():
#    print('blah')
#if __name__ == "__main__":
#    main()
