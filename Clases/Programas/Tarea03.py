def punto (x,y) :
    import math
    d = math.sqrt ( (x-15)**2 + (y-20)**2 )
    return d
    
def diana1 (x,y) :
    if y > 30 and x < 5 :
        return 3
    if y >= 10 and y <= 30 and x < 5 :
        return 5
    if y < 10 and x < 5 :
        return 3
    if y > 30 and x >= 5 and x <=25 :
        return 7
    if y < 10 and x >= 5 and x <= 25 :
        return 7
    if y > 30 and x > 25 :
        return 3
    if y >= 10 and y <= 30 and x > 25 :
        return 5
    if y < 10 and x > 25 :
        return 3
    if punto (x,y) < 10 :
        return 10
    else :
        return 100
        
