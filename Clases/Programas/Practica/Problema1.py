def ex_F (Fmin,Fmax,n) :
    F = []
    dF = (Fmax-Fmin)/float (n-1)
    for i in range (n) :
        f = Fmin + i*dF
        F.append(f)
    return F

def ex_C (F) :
    C = []
    for x in F :
        c = (x-32)*(5/9.0)
        C.append(c)
    return C

def aprox_C (F) :
    C1 = []
    for x in F :
        c1 = (x-30)-2
        C1.append(c1)
    return C1

def dif (C,C1) :
    D = []
    for a in C :
        for b in C1 :
            d = abs(a-b)
            D.append(d)
        return D

def columnas (F,C,C1,D) :
    print '   F       C        C1       D'
    for i in range(len(F)) :
        c = C[i]
        f = F[i]
        c1 = C1[i]
        d = D[i]
        print "%8.1f %8.1f %8.1f %8.1f" % (f,c,c1,d)

