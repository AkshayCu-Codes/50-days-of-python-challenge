def convert_numbers(lst):
    return [f'{num:,}' for num in lst]

print(convert_numbers([120000,12340000,100000]))