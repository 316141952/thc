#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''
import Problema8
from Problema8 import prim_o_comp as poc
x = input ("¿Cuál número natural quieres saber si es primo o compuesto?")
print 'El %d es %s' % (x,poc(x))
