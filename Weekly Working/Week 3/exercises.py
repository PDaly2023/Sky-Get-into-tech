orig = 'ThisIsAReallyLongStringThatIsFunToConvert'
orig2 = 'this_is_a_really_long_string_that_is_fun_to_convert'
def pascal_to_snake(s):
    # Convert the first letter to lowercase
    s = s[0].lower() + s[1:]
    # Add an underscore before each subsequent uppercase letter
    snake = ""
    for c in s:
        if c.isupper():
            snake += "_"
        snake += c.lower()
    return snake

print("output =", pascal_to_snake(orig))


snake_string = "this_is_a_really_long_string_that_is_fun_to_convert"
#create a list using all the words in the string but split them around _
snake_list = snake_string.split("_")
print (snake_list)
#use .title to capitilise every word then use .join to join them together
print(''.join([i.title() for i in snake_list]))

