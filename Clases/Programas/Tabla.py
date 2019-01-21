import grados
from grados import listaC as c
from grados import listaF as f

gradosC = c (-5, 0.5, 5)
gradosF = f (gradosC)
x = zip (gradosC,gradosF)
a = x.pop (0); list (a)
b = x.pop (1); list (b)
c = x.pop (2); list (c)

L = []
L.append (list(a))
L.append (list(b))
L.append (list(c))

print L



