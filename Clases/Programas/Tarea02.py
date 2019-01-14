# -*- coding: utf-8 -*-
t = 20
v = 15
a = 1.5
x1 = v * t #camión
x2 = 1.0/2 * a *t**2 #automóvil
print 'La posición en que se encuentran en el t = %g es x1 = %d para el camión y x2 = %d para el automóvil' % (t,x1,x2)

def pos(t,a,v):
    x1 = v * t
    x2 = 1.0/2 * a * t**2
    return(x1,x2)

