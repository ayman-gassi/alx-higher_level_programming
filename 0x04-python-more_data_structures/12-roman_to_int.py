#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a roman numeral to an integer
    You can assume the number will be between 1 to 3999.
    If the roman_string is not a string or None, return 0
    """
    if type(roman_string) != str or roman_string is None:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    list = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_d[roman_string[i]] > roman_d[roman_string[i - 1]]:
            list += roman_d[roman_string[i]] - 2 * roman_d[roman_string[i - 1]]
        else:
            list += roman_d[roman_string[i]]
    return list
