import math
from math import sqrt as rc

def Fib (n) :
    while n > 0 :
        n = ((1 + rc(5))**n - (1 - rc(5))**n)/(2**n * rc(5))
        return (n)
    
