# -*- coding: utf-8 -*-
def fib (n) :
    ''' Calcula el enésimo término de la
sucesión de Fibonacci con n natural '''
    if n > 2:
        return fib(n-1) + fib (n-2)
    else :
        return 1

fib (1)
fib (2)
fib (5)
fib (10)

def suma (x) :
    if x == 1 :
        return 1
    else :
        return x + suma (x-1)

suma (1)
suma (3)
suma (5)

def recursiva (L) :
    n = len (L)
    if n > 1 :
        print L[0],
        recursiva (L[1:])
    else :
        print L[0]

def printr (L) :
    if L:
        print L [0],
        printr (L [1:])
    else :
        None

http://www.pythontutor.com/visualize.html  
