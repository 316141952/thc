# -*- coding: utf-8 -*-
# Valeria 
print 34 * 3 - (1.0/2) * 9.81 * 3**2 # 1.0/2 división flotante "real"
print 34 * 3 - (1/2) * 9.81 * 3**2  # 1/2 división entera
print 34 * 1 - (1.0/2) * 9.81 * 1**2
print 34 * 1.5 - (1.0/2) * 9.81 * 1.5**2
print 34 * 5 - (1.0/2) * 9.81 * 5**2 
V0 = 34
g = 9.81
t = 5
y = V0 * t - 1.0/2 * g * t**2
print y  
