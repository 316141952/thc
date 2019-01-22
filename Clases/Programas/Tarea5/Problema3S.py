#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

import Problema3
from Problema3 import *

x = input ("¿Cuál es el extremo izquierdo del intervalo?")
y = input ("¿Cuál es el extremo derecho del intervalo?")
n = input ("¿Cuántos subintervalos?")
C = listaC (x,y,n)
F = listaF (C)
print C
print F
