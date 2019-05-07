# -*- coding: utf-8 -*-


########################################################

import numpy as np
import matplotlib.pyplot as plt


"""
Implementar una funcion H_WH(N) que devuelva la matriz NxN asociada a la transformación de Walsh-Hadamard

H_WH(4)=
      [[ 0.5,  0.5,  0.5,  0.5],
       [ 0.5,  0.5, -0.5, -0.5],
       [ 0.5, -0.5, -0.5,  0.5],
       [ 0.5, -0.5,  0.5, -0.5]]
"""

def H_WH(N):
	# matrix creation
	H = np.full((N,N), 1)	
	# initialization
	i1 = 1
	while i1 < N:
		for i2 in range(i1):
			for i3 in range(i1):
				H[i2+i1][i3]    = H[i2][i3]
				H[i2][i3+i1]    = H[i2][i3]
				H[i2+i1][i3+i1] = -1 * H[i2][i3]
		i1 += i1
	return H

print(H_WH(1))
print(H_WH(2))
print(H_WH(4))
print(H_WH(8))
print(H_WH(16))


"""
Implementar la DWHT (Discrete Walsh-Hadamard Transform) y su inversa
para bloques NxN

dwht_bloque(p) 
idwht_bloque(p) 

p bloque NxN

dwht_bloque(
            [[217,   8, 248, 199],
             [215, 189, 242,  10],
             [200,  65, 191,  92],
             [174, 239, 237, 118]]
            )=
            [[ 661,   -7.5, -48.5, 201],
             [   3,  -27.5,  25.5,  57],
             [  59,  -74.5,  36.5, -45],
             [ -51, -112.5, 146.5,  45]]

"""
'''
def dwht_bloque(p):




def idwht_bloque(p):
'''

"""
Reproducir los bloques base de la transformación para los casos N=4,8,16
Ver imágenes adjuntas
"""


