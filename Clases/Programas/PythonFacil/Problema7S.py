#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí está la parte interactiva.
Redefiní la función con el nombre que le
dí y cambié el 1 por una x pues al correr
la función marcaba error por el 1.
'''
import Problema7
from Problema7 import suma_lista as s

x = input ('''Dame la lista de la cual
quieres saber la suma de los elementos: ''')
print 'La suma es de %f' % (s(x))
