original_string = 'ThisIsAReallyLongStringThatIsFunToConvert'

# Convert from PascalCase to snake_case
snake_string = ''.join(['_' + i.lower() if i.isupper() else i for i in original_string]).lstrip('_')

print(snake_string)
