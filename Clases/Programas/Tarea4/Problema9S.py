#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
# Es un programa que te da el área, perímetro y altura
# de cualquier triángulo, y el tipo de triángulo
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''
import Problema9

from Problema9 import trian as t
from Problema9 import perimetro as p
from Problema9 import altura as h
from Problema9 import area as A

a,b,c = input ("Dame las medidas de los tres lados del triángulo :")

print 'El triángulo es %s' % (t(a,b,c))
print 'El perímetro del triángulo es %f' % (p(a,b,c))
print 'El altura del triángulo es %f' % (h(a,b,c))
print 'El área del triángulo es %f' % (A(a,b,c))






