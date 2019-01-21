# -*- coding: utf-8 -*-
# Es un programa que te da el área, perímetro y altura
# de cualquier triángulo, y el tipo de triángulo


def trian (a,b,c) :
    while a > 0 and b > 0 and c > 0 :
        if a == b == c :
            return 'Equilatero'
        if a != b != c != a :
            return 'Escaleno'
        if a == b != c or a == c != b or b == c != a :
            return 'Isosceles'

def perimetro (a,b,c) :
    if trian (a,b,c) == 'Equilatero' :
        P = 3*a
        return P
    if trian (a,b,c) == 'Escaleno' or 'Isosceles' :
        P = a+b+c
        return P

import math
from math import sqrt as rc

def altura (a,b,c) :
    if trian (a,b,c) == 'Equilatero' :
        h = (rc(3)/2.00)*a
        return h
    if trian (a,b,c) == 'Escaleno' or 'Isosceles' :
        s = (a+b+c)/2
        h = (2.00/a)*rc(s*(s-a)*(s-b)*(s-c))
        return h

import math
from math import sqrt as rc

def area (a,b,c) :
    if trian (a,b,c) == 'Equilatero' :
        A = (rc(3)/4.00)*(a**2)
        return A
    if trian (a,b,c) == 'Escaleno' or 'Isosceles' :
        s = (a+b+c)/2
        A = (a*((2.00/a)*rc(s*(s-a)*(s-b)*(s-c))))/2.00
        return A 
    

    


