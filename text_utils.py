def reverse_string(s):
    new_string = []
    for char in s:
        new_string.insert(0, char)
    return "".join(new_string)
#         # function to reverse a string

def capitalize_string(s):
    return s.upper()
#         # function to capitalize a string