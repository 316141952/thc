#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí está la parte interactiva.
Bueno, convenientemente justo había resuelto este mismo problema desde
la tarea 4.
'''
import Problema3
from Problema3 import prim_o_comp as poc
x = input ("¿Cuál número natural quieres saber si es primo o compuesto?")
print 'El %d es %s' % (x,poc(x))
