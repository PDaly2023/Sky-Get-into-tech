def multiply_2_values(*, x, y = 10,):
    return x * y

#now fails because i forced named only arguements using *

#like forcing named arguements, the asterix can be added mid line, forcing all after it to require a name when being called

# print('by default',multiply_2_values(2,))
# print('by position, overwriting default y',multiply_2_values(2, 30 ))

#works as thenamed arguements are called
print('by name, overwriting default y',multiply_2_values(x=50, y=40))


