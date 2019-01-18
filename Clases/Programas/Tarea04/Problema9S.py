#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
Hay que considerar que el circuncentro es un punto que se encuentra
sobre el segmento de recta que representa la altura del triángulo,
y que ahí mismo coinciden el baricentro, ortocentro e incentro
'''
import Problema9

from Problema9 import perimetro as P
x = input ("Para calcular el perímetro introduce la medida de un lado del triángulo :")
print 'El perímetro del triángulo es %f' % (P(x))

from Problema9 import area as A
x = input ("Para calcular el área introduce la medida de un lado del triángulo :")
print 'El área del triángulo es %f' % (A(x))

from Problema9 import altura as h
x = input ("Para calcular la atura introduce la medida de un lado del triángulo :")
print 'La altura del triángulo mide %f' % (h(x))

from Problema9 import apotema as a
x = input ("Para calcular el apotema introduce la medida de un lado del triángulo :")
print 'El apotema del triángulo mide %f' % (a(x))

from Problema9 import circuncentro as c
x = input ("Para calcular el circuncentro introduce la medida de un lado del triángulo :")
print 'El circuncentro está en la altura %f' % (c(x))
