def mcd (a,b):
    while a > b :
        if a%b == 0 :
            return (b)
        else :
            if a%(a%b) == 0 :
                return (a%b)
    
