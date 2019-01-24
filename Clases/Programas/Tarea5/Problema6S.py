#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

from Problema7 import prom10 as p
L = input ("Dame una lista con los 10 datos que quieras promediar")
print 'El promedio es %f' % (p(L))
