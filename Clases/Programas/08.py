#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Este programa fue para aprender cómo ejecutar un programa de python en bash.
''' 
x = 10.5; y = 1.0/3; z = 15.3
#x,y,z = 10.5, 1.0/3, 15.3
H = '''
El punto en R3 es :
(x,y,z) = (%.2f,%g,%G)
''' % (x,y,z) 
print H

G = '''
El punto en R3 es:
(x,y,z) = ({laX:.2f}, {laY:g}, {laZ:G})
''' .format(laX = x,laY = y,laZ = z)
print G

x=input("Cuál es el valor al que le quieres calcular la raíz")
import math as m
from math import sqrt
from math import sqrt as s
from math import * #no se recomienda
print 'la raiz cuadrada de %2.f es %f' % (x,m.sqrt(x))

print sqrt (16.5)
print s (16.5)
