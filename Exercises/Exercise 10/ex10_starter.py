import sys
import glob
import os

# Get the directory name
if sys.platform == 'win32':
    #added extra path info as my home directory is c:\users\admin - used / as python accepts it. could have used \\ (second \ to cancelin build \ meaning)
    hdir = os.environ['HOMEPATH'] = 'C:/Users/Admin/Documents/QA evening learning/Chris Beagles/maxexercise10/exercise10/'
else:
    hdir = os.environ['HOME']

# Construct a portable wildcard pattern
pattern = os.path.join(hdir, '*')


#Use the glob.glob() function to obtain the list of filenames
print(glob.glob(hdir))
files = glob.glob(pattern)
print("")
print("******files within this folder****") #use \n for new line and .join to present each element in list on new line
print("\n" .join(files))
print("")



#use os.path.getsize to find each file's size
#Add a test to only display files that do not have a size of zero
print("******size of each file****")
for filename in glob.glob(pattern): #glob.glob returns a list. getsize expects individual files. iterating over that list gives each individual file and size.
    if os.path.getsize(filename) != 0: #add test to detect if a file size is 0. if it is. ignore it
        print(os.path.getsize(filename))
print("")



#Remove the leading directory name(s) from each filename before you print it
print("******each file without it's path****")
for filename in glob.glob(pattern): #glob.glob returns a list. os.path.basenameindividual files. iterating over that list gives each individual file without the path
    print(os.path.basename(filename))
print("")
#bizarre refomatting occuring when adding/removing newlines or empty strings to create newlines. ask Chris :)
