# -*- coding: utf-8 -*-
# Es una función que determina si un número es primo o compuesto.

def prim_o_comp (x) :
    while x > 0 :
        if x == 2 or x == 3 or x == 5 or x == 7 :
            return 'Primo'
        if x%2 == 0 :
            return 'Compuesto'
        if x%3 == 0 :
            return 'Compuesto'
        if x%4 == 0 :
            return 'Compuesto'
        if x%5 == 0 :
            return 'Compuesto'
        if x%6 == 0 :
            return 'Compuesto'
        if x%7 == 0 :
            return 'Compuesto'
        if x%8 == 0 :
            return 'Compuesto'
        if x%9 == 0 :
            return 'Compuesto'
        if x%10 == 0 :
            return 'Compuesto'
        else :
            return 'Primo'
    
