
def prom10 (x1,x2,x3,x4,x5,x6,x7,x8,x9,x10) :
    L = [x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]
    n = 0
    for x in L :
        n = n + x
    print float(n)/len(L)
