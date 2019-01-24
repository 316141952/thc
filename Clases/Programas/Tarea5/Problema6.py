def prom10 (L) :
    ''' Calcula el promedio de
una lista de 10 números '''
    while len (L) == 10 :
        n = 0
        for x in L :
            n = n + x
        return float(n)/len(L)
