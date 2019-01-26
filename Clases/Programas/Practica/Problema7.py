import math
from math import pi,sin

def H_eps (x,eps = 0.01) :
    if x < -eps :
        return 0
    elif x > eps :
        return 1
    elif -eps <= x <= eps :
        H = (1/2.0 + x/(2*eps) + (1/(2*eps))*(sin((pi*x)/eps)))
        return H

def prueba_H_eps (x,eps = 0.01) :
    n = H_eps (x,eps = 0.01)
    return n

print prueba_H_eps (-1) #x < -eps
print prueba_H_eps (-0.01) #x = -eps
print prueba_H_eps (0) #x = 0
print prueba_H_eps (0.01) #x = eps
print prueba_H_eps (1) # x > -eps
    
