# -*- coding: utf-8 -*-
"""

"""
import math
import numpy as np
import matplotlib.pyplot as plt

'''
Dada una lista p, decidir si es una distribución de probabilidad (ddp)
0<=p[i]<=1, sum(p[i])=1.
'''
def es_ddp(p,tolerancia=10**(-5)):
    sum = 0.0
    for prob in p:
        sum += prob
        if (prob > 1) or (prob < 0):
            return False
    return math.isclose(sum, 1, rel_tol=tolerancia)


'''
Dado un código C y una ddp p, hallar la longitud media del código.
'''

def LongitudMedia(C,p):
    sum = 0.0
    C.sort(reverse=True)

    for n in range(len(C)):
        sum += (len(C[n])*p[n])
    return sum
    
'''
Dada una ddp p, hallar su entropía.
'''
def H1(p):
    sum = 0.0
    for pr in p:
        if (pr != 0):
            sum -= pr*np.log2(pr)
    return sum

'''
Dada una lista de frecuencias n, hallar su entropía.
'''
def H2(n):
    #Hacer la suma de todos y dividir todos los valores por la suma. punto a punto. Despues llamar a h1
    sum = 0.0
    for f in n:
        sum += f
   
    p = []
    for f in n:
        p.append(float(f)/sum)
    return H1(p)

'''
Ejemplos
'''
C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.5,0.1,0.1,0.1,0.1,0.1,0]
n=[5,2,1,1,1]


print(es_ddp(p))

print(H1(p))
print(H2(n))
print(LongitudMedia(C,p))



'''
Dibujar H(p,1-p)
'''
p2 = np.array(p)
p2 = -p2+1
plt.plot(p, p2)
plt.show()





