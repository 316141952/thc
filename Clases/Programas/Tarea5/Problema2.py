#def tiempos (v,y) :
#    Pelota = [v,y]
#    g = 9.81
#    import math
#    from math import sqrt as rc
#    if 0 <= y <= (v*(3-2*v)/g) :
#        t1 = (-v + rc(v**2 + 2*g*y))/(-g)
#        t2 = (-v - rc(v**2 + 2*g*y))/(-g)
#        a = list (t1)
#        b = list (t2)
#        P.append (zip(t1,t2))
#        return Pelota

def tiempos (v,y) :
    T = []
    g = 9.81
    import math
    from math import sqrt as rc
    while 0 <= y :
        t1 = (-v + rc(v**2 + 2*g*y))/g
        t2 = (-v - rc(v**2 + 2*g*y))/g
        T.append (t1)
        T.append (t2)
        return T

def mostrarTiempos (T) :
    for i in range (len(T)) :
        t = T[i]
        print "%5.5f" % (T[i]) 
