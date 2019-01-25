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

def prueba_H
    
