#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Return a list of common elements between two sets
    """
    return list(set(set_1) & set(set_2))
