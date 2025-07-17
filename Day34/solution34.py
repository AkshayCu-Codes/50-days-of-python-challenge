import re

def just_digits():
    with open('python.csv', 'r', encoding='utf-8') as file:
        text = file.read()
    # Use regular expression to find all digit sequences
    digits = re.findall(r'\d+', text)
    return digits