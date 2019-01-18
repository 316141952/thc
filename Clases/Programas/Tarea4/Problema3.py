def C_F (x,y) :
    if x == 'Celsius' or x == 'Farenheit' :
        while x == 'Celsius' :
            g = (y*1.8)+32
            return g
        while x == 'Farenheit' :
            g = (y-32)/1.8
            return g
        
