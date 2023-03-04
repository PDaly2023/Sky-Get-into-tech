string = "Humpty Dumpty sat on a wall"
#if done with no args it will split at easch space
print(string.split())
#split it by the u
print(string.split('u'))

#make u_split a varaible and then use the .join method to rejoin it about the u
u_split = string.split('u')
print('u'.join(u_split))

#string.splitlines() useful with files with lines to move onto the next line
#splits on the newline spereator