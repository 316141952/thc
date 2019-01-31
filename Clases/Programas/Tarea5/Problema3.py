#def listaC (x,y,n) :
#    gradosC = []
#    dC = (x-y)/float (n-1)
#    for i in range (n) :
#        C = x + i*dC
#        gradosC.append (C)
#    return gradosC

#def listaF (gradosC) :
#    gradosF = []
#    for C in gradosC :
#        F = (9.0/5)*C + 32
#        gradosF.append(F)
#    return gradosF

#def lista1F (x,y,n) :
#    gradosF = []
#    dF = (x-y)/float(n-1)
#    for i in range (n) :
#        F = x + i*dF
#        gradosF.append (F)
#    return gradosF

#def lista1C (gradosF) :
#    gradosC = []
#    for F in gradosF :
#        C = (5.0/9)(F-32)
#        gradosC.append (C)
#    return gradosC

def grados (g,x,y,n) :
    if g == 'Celsius' or x == 'Farenheit' :
        while g == 'Celsius' :
            gradosC = []
            dC = (x-y)/float (n-1)
            for i in range (n) :
                C = x + i*dC
                gradosC.append (C)
            return gradosC
            gradosF = []
            for C in gradosC :
                F = (9.0/5)*C + 32
                gradosF.append(F)
            return gradosF
        while g == 'Farenheit' :
            gradosF1 = []
            dF = (x-y)/float(n-1)
            for i in range (n) :
                F1 = x + i*dF
                gradosF1.append (F1)
            return gradosF1
            gradosC1 = []
            for F1 in gradosF1 :
                C1 = (5.0/9)(F1-32)
                gradosC1.append (C1)
            return gradosC1
