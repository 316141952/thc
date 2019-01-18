# -*- coding: utf-8 -*-
# Es un programa que te da el área, perímetro, altura, apotema y circuncentro
# de cualquier triángulo equilátero con las medidas de los lados

def perimetro (x) :
    P = 3*x
    return P

import math
from math import sqrt as rc
def altura (x) :
    h = (rc(3)/2.00)*x
    return h

def area (x) :
    A = (rc(3)/4.00)*x**2
    return A

def apotema (x):
    a = (rc(3)/6.00)*x
    return a

def circuncentro (x):
    c = (rc(3)/6.00)*x**2
    return c
