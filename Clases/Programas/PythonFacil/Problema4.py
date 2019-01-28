# -*- coding: utf-8 -*-
def lista_infinita () :
    i = 1
    while True :
        yield i
        i += 1

def multiplos (x) :
    i = 0
    for n in lista_infinita () :
        yield i
        i = n*x

#for a in multiplos(2) :
#    print a
#Este fue el ejemplo que usé para probar la función.
