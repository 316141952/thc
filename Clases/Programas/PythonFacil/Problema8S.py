#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí está la parte interactiva.
'''
import Problema8
from Problema8 import dif_mayor as dm

x = input ('''Dame la lista: ''')
print '''El valor absoluto de la mayor
diferencia entre los elementos es %f ''' % (dm(x))
