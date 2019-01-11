# -*- coding: utf-8 -*-
i = 62
r = 189876545.7654675432

# Print out numbers with quotes "" such that we see the
# width of the field
print '"%d"' % i       # minimum field
# la parte entera del número
print '"%5d"' % i      # field of width 5 characters
# usar espacio para 5 cifras 
print '"%05d"' % i     # pad with zeros
# acomapñar la cifra con 5 ceros a la izquierda
print '"%g"' % r       # r is big number so this is scientific notation
# como r es un número muy grande se expresa en notación científica
print '"%G"' % r       # E in the exponent
# se utiliza E en el exponente
print '"%e"' % r       # compact scientific notation
# compactar notación científica
print '"%E"' % r       # compact scientific notation
# compactar notación científica
print '"%20.2E"' % r   # 2 decimals, field of width 20
# usar espacio para 20 cifras y usar 2 decimales
print '"%30g"' % r     # field of width 30 (right-adjusted)
# usar el espacio para 3 cifras 
print '"%-30g"' % r    # left-adjust number
# ajustar el número a la izquierda
print '"%-30.4g"' % r  # 3 decimals
# ajustar el número a la izquierda con 3 decimales 
print '%s' % i   # can convert i to string automatically
# convierte i en una cadena automáticamente 
print '%s' % r
# convierte r en una cadena automáticamente

# Use %% to print the percentage sign
# usa %% para mostrar el signo de porcentaje  
print '%g %% of %.2f Euro is %.2f Euro' % \
      (5.1, 346, 5.1/100*346)
