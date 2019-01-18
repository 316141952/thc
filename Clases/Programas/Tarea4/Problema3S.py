#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí probé algunos ejemplos para comprobar la función,
y después puse una parte interactiva para el bash.
'''
import Problema3 
from Problema3 import C_F as g

x = input("Escribe en una cadena el tipo de grados que tienes y quieres convertir :")
y = input("¿Cuántos grados son?")
if x == 'Celsius' :
    print '%f grados Celsius son %f grados Farenheit' % (y,g(x,y))
if x == 'Farenheit' :
    print '%f grados Farenheit son %f grados Celsius' % (y,g(x,y))
    


