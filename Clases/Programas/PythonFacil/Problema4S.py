#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí está la parte interactiva.
'''
import Problema4
from Problema4 import *

x = input ('''Dame el número del cual
quieres saber sus múltiplos: ''')
for a in multiplos (x) :
    print a
