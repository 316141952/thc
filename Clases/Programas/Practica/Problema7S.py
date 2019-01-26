#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
'''
Valeria Ortiz Cervantes, 316141952
Taller de Herramientas Computacionales
Aquí puse la parte interactiva, la verdad este
ejercicio fue relativamente fácil, al principio
no me salía en clase pero porque no estaba en
orden la ecuación de H, acomodé los
paréntesis y todo y salió.
Bueno volví a escribir la función aquí porque cuando la
importaba del Problema 7 no me dejaba de mostrar también
los ejemplos que puse ahí mismo, y como son parte del
ejercicio no quise quitarlos.
'''

def H (x,eps = 0.01) :
    if x < -eps :
        return 0
    elif x > eps :
        return 1
    elif -eps <= x <= eps :
        H = (1/2.0 + x/(2*eps) + (1/(2*eps))*(sin((pi*x)/eps)))
        return H

x = input ("Dame el valor de x: ")
e = input ('''La epsilon base es de 0.01, ¿quieres
definir otra epsilon?(escribe la respuesta en una cadena) ''')
if e == 'No' or e == 'no' :
    eps = 0.01
if e == 'si' or e == 'Si' :
    eps = input ("Dame el valor de epsilon: ")
print H (x,eps) 
