#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''
import Problema3 as p
from Problema3 import CaF
from Problema3 import FaC

C=input("Para convertir grados Celsius a Farenheit. ¿Cuántos grados Celsius? :")
print '%f ºC son %f ºF' % (C,CaF(C))

F=input("Para convertir grados Farenheit a Celsius. ¿Cuántos grados Farenheit?")
print "%f ºF son %f ºC" % (F,FaC(F))
