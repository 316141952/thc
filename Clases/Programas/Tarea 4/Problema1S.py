#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''
import Problema1 as p
p.mcd (30,10)
p.mcd (3000,1000)
p.mcd (400,48)
p.mcd (721, 3)
p.mcd (825, 5)

from Problema1 import mcd 
a=input("¿De qué números quieres calcular el M.C.D.? Número mayor :")
b=input("Número menor :")
print 'El M.C.D. de %d y %g es %d' %(a,b,mcd(a,b))
