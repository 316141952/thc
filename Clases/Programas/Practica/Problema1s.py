#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí puse la parte interactiva, el ejemplo con
el que yo estuve trabajando fue a = -10, b = 10 y n = 10
'''

import Problema1
from Problema1 import *

a = input ("¿Cuál es el extremo izquierdo del intervalo?")
b = input ("¿Cuál es el extremo derecho del intervalo?")
n = input ("¿Cuántos subintervalos?")

F = ex_F (a,b,n)
C = ex_C (F)
C1 = aprox_C (F)
D = dif (C,C1)
print '''La tabla con las diferencias entre la
fórmula exacta y la aproximada es la siguiente:'''
print columnas (F,C,C1,D)

