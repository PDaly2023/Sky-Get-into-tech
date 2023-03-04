snake_string = "this_is_a_really_long_string_that_is_fun_to_convert"

snake_list = snake_string.split("_")

print(''.join([i.title() for i in snake_list]))
