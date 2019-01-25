IntPositivDiagonal = [(3.5,2.5),(4,4),(4.5,5.5),(5,7)]

IntPositiv = [(3.5,4),(3.5,5.5),(3.5,7),(4,2.5),(4,5.5),
               (4,7),(4.5,2.5),(4.5,4),(4.5,7),(5,2.5),
               (5,4),(5,5.5),IntPositivDiagonal]

IntNegatDiagonal = [(-3.5,-2.5),(-4,-4),(-4.5,-5.5),(-5,-7)]

IntNegat = [(-3.5,-4),(-3.5,-5.5),(-3.5,-7),(-4,-2.5),(-4,-5.5),
             (-4,-7),(-4.5,-2.5),(-4.5,-4),(-4.5,-7),(-5,-2.5),
             (-5,-4),(-5,-5.5),IntNegatDiagonal]

IntYNegatDiagonal = [(3.5,-2.5),(4,-4),(4.5,-5.5),(5,-7)]

IntYNegat = [(3.5,-4),(3.5,-5.5),(3.5,-7)(4,-2.5),(4,-5.5),
               (4,-7),(4.5,-2.5),(4.5,-4),(4.5,-7),(5,-2.5),
               (5,-4),(5,-5.5),IntYNegatDiagonal]

IntXNegatDiagonal = [(-3.5,2.5),(-4,4),(-4.5,5.5),(-5,7)]

IntXNegat = [(-3.5,4),(-3.5,5.5),(-3.5,7),(-4,2.5),(-4,5.5),
               (-4,7),(-4.5,2.5),(-4.5,4),(-4.5,7),(-5,2.5),
               (-5,4),(-5,5.5),IntXNegatDiagonal]


Malla = [IntPositiv , IntNegat , IntYNegat , IntXNegat]

#print Malla

def malla (inX,finX,incrX,inY,finY,incrY) :
    M = []
    x = inX
    y = inY
    while x and y > 0 :
        while x <= finX :
            x += incrX
        while y <= finY :
            y += incrY
        M.append((x,y))
    while x and y < 0 :
        while x <= -finX :
            x -= incrX
        while y <= -finY:
            y -= incrY
        M.append((x,y))
    while x < 0 and y > 0 :
        while x <= -finX :
            x -= incrX
        while y <= finY :
            y += incrY
        M.append((x,y))
    while x > 0 and y < 0 :
        while x <= finX :
            x += incrX
        while y <= -finY:
            y -= incrY
        M.append((x,y))
    print M
