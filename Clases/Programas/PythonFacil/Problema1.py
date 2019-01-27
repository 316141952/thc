def listas (L1,L2) :
    if len (L1) == len (L2) :
        for i in range(len(L1)) :
            for j in range(len(L2)) :
                if L1[i] == L2[j] :
                    return 'son iguales'
                else :
                    return 'no son iguales'
                    
    else :
        return 'no son iguales'
