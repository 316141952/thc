# -*- coding: utf-8 -*-
#def g (1) :
#    a = 0
#    for i in 1 :
#        for j in 1 :
#            if abs (i-j) > a :
#                a = abs (i-j)
#    return a 

'''El problema consiste en determinar el
propósito de la función g y darle un buen
nombre.
El propósito de la función g es dar el
valor absoluto de la mayor diferencia
entre los elementos de una lista; aunque
también creo que definir la a como 0 es
innecesario pues es mejor solo poner el 0
y que se tiene que cambiar el 1 por una
constante pues sino al correr la función
marca un error ahí.
Yo creo que un buen nombre sería dif_mayor.
'''

def dif_mayor (x) :
    a = 0
    for i in x :
        for j in x :
            if abs (i-j) > a :
                a = abs (i-j)
    return a 
