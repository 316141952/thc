#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí está la parte interactiva.
'''

import Problema2
from Problema2 import *

v = input ("¿Cuál es la velocidad inicial de la pelota? ")
y = input ("¿Cuál es la altura de la pelota? ")
T = tiempos (v,y)
print '''Los tiempos en los que se encuentra a esa altura
son:'''
print mostrarTiempos(T)
