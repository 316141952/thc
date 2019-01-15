# -*- coding: utf-8 -*-
def vAbsoluto (x) :
    if x >= 0 :
        return (x)
    else:
        return (-x)

def raiz (x) :
    h = x
    b = 1.0
    e = 0.0001
    i = 0 #cuenta el número de veces que se ejecuta el ciclo
    while vAbsoluto (b-h) > e :
        h = ( b+h )/2
        b = x/h
        i = i + 1
    print "EL ciclo se repitió %d veces" %(i)
    return (b)

def raiz1 (x) :
    h = x
    b = 1.0
    e = 0.0001 #representa el error, decimales de precisión
    while vAbsoluto (b-h) > e :
        h = ( b+h )/2
        b = x/h
        print (h)
        print (b)
    return (b)    

print raiz (1)
print raiz (4)
print raiz (9)
print raiz (9.1)
print raiz (1000000)
print raiz1 (4)
