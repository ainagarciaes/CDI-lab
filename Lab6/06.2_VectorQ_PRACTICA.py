# -*- coding: utf-8 -*-
"""

"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
from scipy.cluster.vq import vq, kmeans
from skimage import io
import math
#%%

#imagen=scipy.misc.imread('../standard_test_images/house.png')
imagen = io.imread('./Imatges/house.png')
(n,m)=imagen.shape # filas y columnas de la imagen
plt.figure()    
plt.imshow(imagen, cmap=plt.cm.gray)
plt.show()

#%%
def kmeansQ(imagen):
    imagen2 = imagen

    x, y = imagen.shape
    blocks = np.zeros((int(x*y/64), 64))

    for i in range (0, x, 8):
        for j in range (0, y, 8):
            curr_block = imagen[i:i+8, j:j+8]
            blocks[int(i*x/64+j/8), :] = np.reshape(curr_block, 64) 

    centr, _ = kmeans(blocks, 512)
    dicc, _ = vq(blocks, centr)

    rnge = int(x/8)

    for i in range (0, rnge*rnge):
        b = centr[dicc[i]]
        for j in range (0, 8*8):
            x = int(8*int(i/rnge) + j/8)
            y = int(j%8 + 8*int(i%rnge))
            imagen2[x][y] = int(b[j])

    return imagen2

def kmeansHouseDic(camera):
    imagen = io.imread('./Imatges/house.png')

    # blocks imatge house
    x, y = imagen.shape
    blocks = np.zeros((int(x*y/64), 64))

    for i in range (0, x, 8):
        for j in range (0, y, 8):
            curr_block = imagen[i:i+8, j:j+8]
            blocks[int(i*x/64+j/8), :] = np.reshape(curr_block, 64) 

    # blocks imatge cameraman
    x2, y2 = camera.shape
    blocks2 = np.zeros((int(x2*y2/64), 64))

    for i in range (0, x2, 8):
        for j in range (0, y2, 8):
            curr_block2 = camera[i:i+8, j:j+8]
            blocks2[int(i*x/64+j/8), :] = np.reshape(curr_block2, 64) 
    
    centr, _ = kmeans(blocks, 512)
    dicc, _ = vq(blocks2, centr)

    rnge = int(x/8)

    for i in range (0, rnge*rnge):
        b = centr[dicc[i]]
        for j in range (0, 8*8):
            x = int(8*int(i/rnge) + j/8)
            y = int(j%8 + 8*int(i%rnge))
            imagen2[x][y] = int(b[j])

    return imagen2
    

"""
Usando K-means http://docs.scipy.org/doc/scipy/reference/cluster.vq.html
crear un diccionario cuyas palabras sean bloques 8x8 con 512 entradas 
para la imagen house.png.

Dibujar el resultado de codificar house.png con dicho diccionario.

Calcular el error, la ratio de compresión y el número de bits por píxel
"""
im = kmeansQ(imagen)

plt.imshow(im, cmap=plt.cm.gray)
plt.show()

x, y = imagen.shape
imagen = io.imread('./Imatges/house.png')
err = np.sqrt(sum(sum(np.subtract(imagen,im)**2))/(x*y))
print("error: ", err)


imSize = x * y * 8 #bytes * 8bits/byte
im2Size =  x * y / 64 * math.ceil(math.log(512,2))
d = 512 * (8*8) * 8

#tamaño del diccionario + el de la imagen comprimida
im2Size = im2Size + d
r = imSize / im2Size
print("ratio:", r)

bitsPixel = 8*im2Size/imSize
print("bits pixel", bitsPixel)

"""
Hacer lo mismo con la imagen cameraman.png

https://atenea.upc.edu/mod/folder/view.php?id=1833385
http://www.imageprocessingplace.com/downloads_V3/root_downloads/image_databases/standard_test_images.zip
"""


"""
Dibujar el resultado de codificar cameraman.png con el diccionarios obtenido
con la imagen house.png

Calcular el error.
"""
print("\nCAMERAMAN\n")
camera = io.imread('./Imatges/cameraman.png')

plt.imshow(camera, cmap=plt.cm.gray)
plt.show()

im = kmeansQ(camera)

camera = io.imread('./Imatges/cameraman.png')
plt.imshow(im, cmap=plt.cm.gray)
plt.show()

x, y = camera.shape

err = np.sqrt(sum(sum(np.subtract(camera,im)**2))/(x*y))
print("error: ", err)