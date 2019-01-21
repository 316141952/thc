#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

import Problema2
from Problema2 import tiempo1 as t1
from Problema2 import tiempo2 as t2

v,y = input ("Dame la velocidad inicial y la posición (en ese orden) :")
print 'El tiempo 1 es %f' % (t1(v,y))
print 'El tiempo 2 es %f' % (t2(v,y))
