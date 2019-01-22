#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

import Problema5
from Problema5 import suma as s

n = input ("¿Hasta qué número quieres calcular la suma?")
print 'La suma de los primeros n naturales, con n = %d, es %d' % (n,s(n)) 
