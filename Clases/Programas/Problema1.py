def mcd (a,b) :
    if a < b :
        tmp = b
        b = a
        a = tmp
    r = a%b
    while r != 0 :
        a = b
        b = r
        r = a%b
    return b

