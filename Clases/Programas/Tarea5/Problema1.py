def mcd (a,b) :
    L = [a,b]
    for x in L :
        if a%b == 0 :
            return (b)
        else :
            if a%(a%b) == 0 :
                return (a%b)
