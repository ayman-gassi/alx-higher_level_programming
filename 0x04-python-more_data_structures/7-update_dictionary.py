#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    a function that replaces or adds key/value in a dictionary.
    key argument will be always a string
    value argument will be any type
    """
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
