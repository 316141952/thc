def sum_cub (x) :
    

def sum_for (x) :
    s = ((x*(x+1))/2)**2
    return s

def comp (n) :
    n1 = sum_cub (n)
    n2 = sum_for (n)
    print "%5.1f %5.1f" % (n1,n2)
