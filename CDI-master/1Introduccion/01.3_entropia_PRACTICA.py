# -*- coding: utf-8 -*-
"""

"""
import math
import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D
'''
Dada una lista p, decidir si es una distribución de probabilidad (ddp)
0<=p[i]<=1, sum(p[i])=1.
'''
def es_ddp(p,tolerancia=10**(-5)):
	for i in p:
		if 0>i or i>1:
			return False
	return (sum(p)>1+ tolerancia) and (sum(p) < 1-tolerancia)



'''
Dado un código C y una ddp p, hallar la longitud media del código.
'''

def LongitudMedia(C,p):
	return sum([len(a)*b for (a,b) in zip (C,p)])

    
'''
Dada una ddp p, hallar su entropía.
'''
def H1(p):
	p= filter(lambda x: x !=0,p)
	return sum(map(lambda x : x*math.log2(1./x),p ))

'''
Dada una lista de frecuencias n, hallar su entropía.
'''
def H2(n):
	m = sum(n)
	p = [x/m for x in n]
	return H1(p)



'''
Ejemplos
'''
C=['001','101','11','0001','000000001','0001','0000000000']
p=[0.5,0.1,0.1,0.1,0.1,0.1,0]
n=[5,2,1,1,1]

print('H1')
print(H1(p))
print('H2')
print(H2(n))
print('longMedia')
print(LongitudMedia(C,p))



'''
Dibujar H(p,1-p)
'''


p= np.arange(0,1,0.01)
q = [1. - x for x in p]
Hpq= [H1([x,y]) for (x,y) in zip(p,q)]
#plt.plot(p, Hpq , 'r-')
#plt.ylabel('H(p,1-p)')
#plt.show()


'''
Hallar aproximadamente el máximo de  H(p,q,1-p-q)
'''
x = []
y = []
z = []
for p in np.arange(0,1,0.02):
	for q in np.arange(0,1-p,0.02):
		x.append(p)
		y.append(q)
		z.append(1-p-q)		

Hpq= [H1([x,y,1-x-y]) for (x,y) in zip(x,y)]
fig= plt.figure()
ax = fig.gca(projection='3d')
ax.scatter(x,y,Hpq)

plt.show()
#parece que el maximo se encuentra cuando las 3 
#variables estan bien equilibradas

