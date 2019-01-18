# -*- coding: utf-8 -*-
# Es un programa que te da el área, perímetro y altura
# de cualquier triángulo 

t == 'Equilátero' or t == 'Isósceles' or t == 'Escaleno'
def perimetro (t,x,y,z) :
    while t == 'Equilátero':
        P = 3*x
        return P
    while t == 'Isósceles' or t == 'Escaleno' :
        P = x+y+z
        return P

import math
from math import sqrt as rc
def altura (t,x,y,z) :
    while t == 'Equilátero':
        h = (rc(3)/2.00)*x
        return h
    

def area (x) :
    A = (rc(3)/4.00)*x**2
    return A


