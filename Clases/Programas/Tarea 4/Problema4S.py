#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''
import Problema4 as p
p.Fib (3)
p.Fib (4)
p.Fib (5)
p.Fib (6)
p.Fib (7)
p.Fib (8)
p.Fib (9)
p.Fib (10)

from Problema4 import Fib
n=input("¿Qué término de la sucesión de Fibonacci quieres calcular?")
print 'El enésimo término de la sucesión de Fibonacci, con n = %g, es %d' % (n, Fib(n))
