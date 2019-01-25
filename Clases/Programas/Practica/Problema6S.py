#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí puse la parte interactiva
'''

import Problema6
from Problema6 import fac as f

n = input ("Dame el número del cual quieras saber su factorial: ")
print 'El factorial de %d es %s' % (n,f(n))
