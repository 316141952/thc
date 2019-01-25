#def sum_c (x) :
#    if n == 1 :
#        return 1
#    else n > 1 :
#        return 1 + sum_c (x-1)

#def sum_c (x) :
#    i = 0
#    while i > 0 :
#        i += 1
#        i += i**2
#    return i

#def sum_c (x) :
#    a = 0
#    b = 0
#    S = []
#    for i in S :
#        while i < x :
#            i += 1
#            a = a + i**2
#            S.append(a)
#            n = S.pop(len(S)-1)
#    print n

#Muchos intentos fallidos pero sí se pudo

def sum_c (x) :
    if x == 1 :
        return 1
    else :
        return x**2 + sum_c (x-1)

def sum_for (x) :
    s = (x*(x+1)*(2*x+1))/6
    return s 

def comp (n) :
    n1 = sum_c (n)
    n2 = sum_for (n)
    print 'Mi programa Formula'
    print "%8.1f %8.1f" % (n1,n2)
