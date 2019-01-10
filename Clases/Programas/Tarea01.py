# -*- coding: utf-8 -*-
# Un automóvil que está parado arranca con una aceleración de 1.5 m/s**2. En ese mismo instante es adelantado por un camión que lleva una velocidad constante de 15 m/s. Calcular la posición de encuentro de ambos vehículos.
x1 = 15 * t #camión
x2 = 1.0/2 * 1.5 *t**2 #automóvil
# Como debemos de calcular la posición cuando se encuentran, las x1 y x2 se igualan y obtenemos la ecuación 0.75t**2-15t=0, cuyas soluciones son t1=0 y t2=20. Ya sabemos que se encontraron cuando el auto arracó, lo cual sería en t0, por lo cual su segundo encuentro sería en t2
t = 20
print x1
print x2
# Y así concluimos que se encuentran cuando ambos llevan 300 m recorridos
