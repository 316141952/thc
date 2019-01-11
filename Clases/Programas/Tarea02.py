# -*- coding: utf-8 -*-
t = 20
x1 = 15 * t #camión
x2 = 1.0/2 * 1.5 *t**2 #automóvil
print 'La posición en que se encuentran en el t = %g es x1 = %d para el camión y x2 = %d para el automóvil' % (t,x1)

def pos(t):
    x1 = 15 * t
    x2 = 1.0/2 * 1.5 * t**2
    return(x1,x2)






