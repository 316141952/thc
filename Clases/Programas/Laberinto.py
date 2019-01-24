L = [[True,True,True,True],
     [False,False,False,True],
     [True,True,False,True]] 
def resolver (L,e) :
    print e # e es la entrada del laberinto
    n = len (L[0])#número de columnas
    m = len (L)
    x = e[0]
    y = e[1]
    if y == n-1 or x == m-1 :
        return e[0]+1, e[1]+1 #en este caso e es la salida
    else :
        if L[x][y+1] == False : #de aquí en adelante e es la posición en la que estás
            e = [x,y+1]
            return resolver (L,e)
        elif L[x+1][y] == False :
            e = [x+1,y] 
            return resolver (L,e)
        else:
            print 'Ya no puede avanzar'

r = resolver (L, [1,0]) 
import numpy as np
print (np.matrix(L))
