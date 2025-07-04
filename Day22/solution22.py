def add_hash(text):
    return '#'.join(text)

def add_underscore(text):
    return text.replace('#','_')

def remove_underscore(text):
    return text.replace('_','')

print(remove_underscore(add_underscore(add_hash('Python'))))  # Output: Python
print(add_hash('Code'))                                       # Output: C#o#d#e
print(add_underscore('P#y#t#h#o#n'))                          # Output: P_y_t_h_o_n
print(remove_underscore('P_y_t_h_o_n'))                       # Output: Python