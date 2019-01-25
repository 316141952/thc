def sum_cub (x) :
    if x == 1 :
        return 1
    else :
        return x**3 + sum_cub (x-1)

def sum_for (x) :
    s = ((x*(x+1))/2)**2
    return s

def comp (n) :
    n1 = sum_cub (n)
    n2 = sum_for (n)
    print 'Mi programa Formula'
    print "%8.1f %8.1f" % (n1,n2)

