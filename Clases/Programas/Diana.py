def diana (x,y) :
    if y > 30 and x < 5 :
        return 3
    if y >= 10 and y <= 30 and x < 5 :
        return 5
    if y < 10 and x < 5 :
        return 3
    if y > 30 and x >= 5 and x <=25 :
        return 7
    if y >= 10 and y <= 30 and x >= 5 and x <= 25 :
        return 10
    if y < 10 and x >= 5 and x<= 25 :
        return 7
    if y > 30 and x > 25 :
        return 3
    if y >= 10 and y <= 30 and x > 25 :
        return 5
    if y < 10 and x > 25 :
        return 3


