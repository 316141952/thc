def tiempos (v,y) :
    Pelota = [v,y]
    g = 9.81
    import math
    from math import sqrt as rc
    t1 = (-v + rc(v**2 + 2*g*y))/(-g)
    t2 = (-v - rc(v**2 + 2*g*y))/(-g)
    a = list (t1)
    b = list (t2) 
    Pelota.append (zip (a,b))
    return Pelota


