# -*- coding: utf-8 -*-


########################################################

# https://github.com/elenaouro/CDI-Compression-of-Data-and-Images-/blob/master/JPEG/07_P_jpeg.py
# https://github.com/xarxax/CDI/blob/master/07JPEG/07_jpeg_PRACTICA.py

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
def Reorder(H_desordenada):
	x, y = np.shape(H_desordenada)
	H_ordenada = np.full((x,y), 1)	

	for i in range(0, x):
		canvis = 0
		for j in range (1, y):
			if (H_desordenada[i, j-1] != H_desordenada[i, j]):
				canvis += 1

		for j in range (0, y):
			H_ordenada[canvis][j] = H_desordenada[i][j]		

	return H_ordenada

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
	H = Reorder(H) 		# reorder the rows
	H = H / np.sqrt(N)	# divide it by sqrt(n)
	return H


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

def dwht_bloque(p):
	x, _ = np.shape(p)
	H = H_WH(x)

	result = np.dot(H, p)
	result = np.dot(result, H)
	
	return result



def idwht_bloque(p):
	x, _ = np.shape(p)
	H = H_WH(x)
	H = np.linalg.inv(H)

	result = np.dot(H, p)
	result = np.dot(result, H)
	
	return result
	
"""
Reproducir los bloques base de la transformación para los casos N=4,8,16
Ver imágenes adjuntas
"""

def printBlock(N):
	H = H_WH(N)
	i = 0

	for row in range(N):
		for col in range(N):
			i += 1
			plt.subplot(N, N, i)
			img = np.tensordot(H[row], np.transpose(H[col]), 0)
			plt.imshow(img)
	plt.show()
	return

printBlock(4)
printBlock(8)
printBlock(16)

