#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

import Problema7
from Problema7 import *

L = input ("Dame una lista con los 10 números")
print 'El promedio es %f' % (prom10(L))
print 'El número mayor de la lista es %d' % (may(L))
print 'El número menor de la lista es %d' % (men(L))
