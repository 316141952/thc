# -*- coding: utf-8 -*-
#def f (1) :
#    a = 0
#    b = 0
#    for i in 1 :
#        if i > 0 :
#            a += i
#        else :
#            a -= i
#    return a + b

'''El problema consiste en determinar el
propósito de la función f y darle un buen
nombre.
El propósito de la función f es dar la
suma de los elementos de una lista
con el valor absoluto de cada número;
algo que noté fue que no debería de estar
la b pues no afecta en nada la función.
Yo creo que un buen nombre sería suma_lista.
'''

def suma_lista (x) :
    a = 0
    for i in x :
        if i > 0 :
            a += i
        else :
            a -= i
    return a 
