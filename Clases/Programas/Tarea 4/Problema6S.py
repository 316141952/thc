#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

import Problema6 as p
p.prom_10 (1,2,3,4,5,6,7,8,9,10)
p.prom_10 (2,4,6,8,10,12,14,16,18,20)
p.prom_10 (3,6,9,12,15,18,21,24,27,30)
p.prom_10 (4,8,12,16,20,24,28,32,36,40)
p.prom_10 (5,10,15,20,25,30,35,40,45,50)

from Problema6 import prom_10 as P
(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10) =input("¿De cuáles 10 datos quieres obtener el promedio?")
print 'El promedio es %g' % (P(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10))
