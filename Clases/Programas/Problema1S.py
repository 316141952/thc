#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales

'''
import Problema1
from Problema1 import mcd
a = input("Dame el entero mayor :")
b = input("Dame el entero menor :")
print 'El M.C.D. de %d y%d es %d' % (a,b,mcd (a,b))
