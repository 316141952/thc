def tiempo1 (v,y) :
    g = 9.81
    import math
    from math import sqrt as rc
    while y >= 0 :
        t1 = (-v + rc(v**2 + 2*g*y))/g
        return t1

def tiempo2 (v,y) :
    g = 9.81
    import math
    from math import sqrt as rc
    while y >= 0 :
        t2 = (-v - rc(v**2 + 2*g*y))/g
        return t2
