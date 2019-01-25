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
