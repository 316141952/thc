def prom10 (L) :
    ''' Calcula el promedio de
una lista de 10 números '''
    while len (L) == 10 :
        n = 0
        for x in L :
            n = n + x
        return float(n)/len(L)

def may (L) :
    '''Calcula el número mayor
de una lista de 10 números'''
    while len (L) == 10 :
        sort (L)
        n = L.pop()
        return n

def men (L) :
    '''Calcula el número menor
de una lista de 10 números'''
    while len (L) == 10 :
        sort (L)
        n = L.pop(0)
        return n
 
