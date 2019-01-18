# -*- coding: utf-8 -*-
# Es un programa que te da el área, perímetro y altura
# de cualquier triángulo 

t == 'Equilátero' or t == 'Isósceles' or t == 'Escaleno'
def perimetro (t,a,b,c) :
    if t == 'Equilátero':
        P = 3*a
        return P
    if t == 'Isósceles' or t == 'Escaleno' :
        P = a+b+c
        return P

import math
from math import sqrt as rc
def altura (t,a,b,c) :
    if t == 'Equilátero':
        h = (rc(3)/2.00)*a
        return h
    if t == 'Isósceles' or t == 'Escaleno' :
        s = (a+b+c)/2
        h = (2/a)*rc(s*(s-a)*(s-b)*(s-c))
        return h
        
def area (t,a,b,c) :
    if t == 'Isósceles' or t == 'Escaleno' :
    A = (a*((2/a)*rc(s*(s-a)*(s-b)*(s-c)))/2
    return A


