#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''

import Problema1
from Problema1 import mcd 
a=input("¿De qué números quieres calcular el M.C.D.? Número mayor :")
b=input("Número menor :")
print 'El M.C.D. de %d y %g es %d' %(a,b,mcd(a,b))
