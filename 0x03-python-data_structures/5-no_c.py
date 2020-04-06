#!/usr/bin/python3
def no_c(my_string):
    replace_chars = ['c', 'C']
    new_str = ''.join(i for i in my_string if not i in replace_chars)
    return new_str
