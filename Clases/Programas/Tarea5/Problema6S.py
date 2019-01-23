#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

from Problema7 import prom10 as p
[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10] = input ("Dame una lista con los 10 datos que quieras promediar")
L = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
for i in L :
    L.pop (i)
    (i, )

print 'El promedio es %f' % (p(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
