#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

from Problema6 import prom_10 as P
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = input("¿De cuáles 10 datos quieres obtener el promedio?")
print "El promedio es %f" % (P(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))

from Problema6 import prom_10 as p
x1 = input ("¿De cuáles 10 datos quieres obtener el promedio?. Primer dato :")
x2 = input ("Segundo dato :")
x3 = input ("Tercer dato :")
x4 = input ("Cuarto dato :")
x5 = input ("Quinto dato :")
x6 = input ("Sexto dato :")
x7 = input ("Séptimo dato :")
x8 = input ("Octavo dato :")
x9 = input ("Noveno dato :")
x10 = input ("Décimo dato :")
print 'El promedio es %f' % (p (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
