def listaC (x,y,n) :
    gradosC = []
    dC = (x-y)/float (n-1)
    for i in range (n) :
        C = Cmin + i*dC
        gradosC.append (C)
    return gradosC

def listaF (gradosC) :
    gradosF = []
    for C in gradosC :
        F = (9.0/5)*C + 32
        gradosF.append(F)
    return gradosF
