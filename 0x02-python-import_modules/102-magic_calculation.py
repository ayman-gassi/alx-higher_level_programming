#!/bin/usr/bin/ptyhon3

def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if (a < b):
        c = add(a, b)
        for z in range(4, 6):
            c = add(c, z)
        return(c)
    return(sub(a, b))
