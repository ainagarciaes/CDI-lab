# -*- coding: utf-8 -*-

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt


import scipy.ndimage
from scipy.cluster.vq import vq, kmeans

#%%
imagen = misc.ascent()#Leo la imagen
(n,m)=imagen.shape # filas y columnas de la imagen
plt.imshow(imagen, cmap=plt.cm.gray) 
plt.xticks([])
plt.yticks([])
plt.show() 
        
"""
Mostrar la imagen habiendo cuantizado los valores de los píxeles en
2**k niveles, k=1..8

Para cada cuantización dar la ratio de compresión y Sigma

Sigma=np.sqrt(sum(sum((imagenOriginal-imagenCuantizada)**2)))/(n*m)

"""

def pixelScalarQ(imagen, k):
    #tamany del interval per la K donada (el 8 es perque la imatge original esta representada amb 8 bits (b&w))
    sh= 2**(8-k+1) 
    #arrodonir cada pixel al valor mes proper segons el tamany d'interval
    img = [[np.round(i /sh) for i in row] for row in imagen] 
    #retornem la imatge comprimida
    return img

# cridem a la funcio per cada un dels valors de K demanats al enunciat
for k in range (1, 8):
    imagenCuantizada = pixelScalarQ(imagen, k)
    print("\n------------ VALOR DE K ", k, " ------------\n")
    ratio_compresion =  8 / k
    Sigma=np.sqrt(sum(sum((imagen-imagenCuantizada)**2)))/(n*m)

    print("Ratio de compresion:", ratio_compresion, "Sigma: ", Sigma)

    plt.imshow(imagenCuantizada, cmap=plt.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.show() 


#%%
"""
Mostrar la imagen cuantizando los valores de los pixeles de cada bloque
n_bloque x n_bloque en 2^k niveles, siendo n_bloque=8 y k=2

Calcular Sigma y la ratio de compresión (para cada bloque 
es necesario guardar 16 bits extra para los valores máximos 
y mínimos del bloque, esto supone 16/n_bloque**2 bits más por pixel).
"""

# TODO