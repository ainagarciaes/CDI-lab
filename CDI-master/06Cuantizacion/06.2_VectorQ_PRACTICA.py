# -*- coding: utf-8 -*-
"""

"""

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage
import math
from scipy.cluster.vq import vq, kmeans

#%%
lena = scipy.misc.imread('../standard_test_images/lena_gray_512.png')
(n, m) = lena.shape  # filas y columnas de la imagen
plt.figure()
plt.xticks([])
plt.yticks([])
plt.imshow(lena, cmap=plt.cm.gray)
# plt.show()



"""FUNCIONES PARA CONVERTIR A BLOQUES Y RECUPERAR"""

def toBlocks(img,fil,col):
    blockImage= np.zeros((int(fil*col/64),8,8))
    block=0
    for i in range(int(col/8)):
        for j in range(int(fil/8)):
            blockImage[block]= np.reshape(img[j*8:j*8+8,i*8:i*8+8],[8,8])
            block+=1
    return blockImage


def fromBlocks(blockImage,fil,col):
    img = np.array([np.array([None]*col) for i in range(fil)])
    z=0
    for i in range(int(col/8)):
        for j in range(int(fil/8)):
            img[j*8:j*8+8,i*8:i*8+8] = blockImage[z]
            z+=1
    return img



"""
Usando K-means http://docs.scipy.org/doc/scipy/reference/cluster.vq.html
crear un diccionario cuyas palabras sean bloques 8x8 con 512 entradas
para la imagen de Lena.

Dibujar el resultado de codificar Lena con dicho diccionario.

Calcular el error, la ratio de compresión y el número de bits por píxel
"""


def quantizarVectorial(imagen, entradas):
	blockImage = toBlocks(imagen, len(imagen),len(imagen[0]))
	flattenedBlocks = [np.ndarray.flatten(np.array(i)) for i in blockImage]
	flattenedBlocks = [[float(i) for i in row] for row in flattenedBlocks]
	#3r parametro num iteraciones
	means, _ = kmeans(flattenedBlocks, entradas)

	intmeans= []
	for i in range(len(means)):
		intmeans.append([])
		for j in means[i]:
			intmeans[i].append(int(j))
	referenced_image,_ = vq(flattenedBlocks,means)
	return referenced_image,intmeans

blockSize= 8
numEntradas=512
pixelBits=8
lenaVec,kvalues =quantizarVectorial(lena,numEntradas)
lenaVec= [np.reshape(kvalues[i],[blockSize,blockSize]) for i in lenaVec]
lenaVec= [[list(row)for row in block]for block in lenaVec]
recoveredLena = fromBlocks(lenaVec,len(lena),len(lena[0]))

print('---------------')
#error
sigma1 = np.sqrt(sum(sum((lena-recoveredLena)**2))/(n*m))
print('error lena: ' + str(sigma1))
#rati compresion
imgSize = len(lena[0]) * len(lena) *pixelBits
numBlocks = len(lena[0]) * len(lena) / (blockSize**2)
#los valores necesitaran un numero de bits proporcional al numero de entradas
encodedImageSize =  numBlocks * math.ceil(math.log(numEntradas,2))
#un bloque a guardar por entrada, cada bloque ocupa blockSize**2 pixeles
dictSize= numEntradas * (blockSize**2) *pixelBits
recoveredImgSize = encodedImageSize + dictSize
ratio_compresion = imgSize / recoveredImgSize
print('ratio compresion lena: ' + str(ratio_compresion))
bitsxPixel= recoveredImgSize / (len(lena[0]) * len(lena))
print('bitsxPixel lena: ' + str(bitsxPixel))
plt.imshow(recoveredLena.astype(np.uint8), cmap=plt.cm.gray)
plt.show()

print('---------------')

"""
Hacer lo mismo con la imagen Peppers (escala de grises)

http://atenea.upc.edu/mod/folder/view.php?id=1577653
http://www.imageprocessingplace.com/downloads_V3/root_downloads/image_databases/standard_test_images.zip
"""
peppers = scipy.misc.imread('../standard_test_images/peppers_gray.png')
(n, m) = peppers.shape  # filas y columnas de la imagen

goodpeppersVec, pepperskvalues= quantizarVectorial(peppers,numEntradas)
goodpeppersVec= [np.reshape(pepperskvalues[i],[blockSize,blockSize]) for i in goodpeppersVec]
goodpeppersVec= [[list(row)for row in block]for block in goodpeppersVec]
goodpeppersVec = fromBlocks(goodpeppersVec,len(peppers),len(peppers[0]))

sigma1 = np.sqrt(sum(sum((peppers-goodpeppersVec)**2))/(n*m))
print('error peppers: ' + str(sigma1))
#ratio compresion
imgSize = len(peppers[0]) * len(peppers) *pixelBits
numBlocks = len(peppers[0]) * len(peppers) / (blockSize**2)
#los valores necesitaran un numero de bits proporcional al numero de entradas
encodedImageSize =  numBlocks * math.ceil(math.log(numEntradas,2))
#un bloque a guardar por entrada, cada bloque ocupa blockSize**2 pixeles
dictSize= numEntradas * (blockSize**2) *pixelBits
recoveredImgSize = encodedImageSize + dictSize
ratio_compresion = imgSize / recoveredImgSize
print('ratio compresion peppers: ' + str(ratio_compresion))
bitsxPixel= recoveredImgSize / (len(peppers[0]) * len(peppers))
print('bitsxPixel peppers: ' + str(bitsxPixel))

plt.imshow(goodpeppersVec.astype(np.uint8), cmap=plt.cm.gray)
plt.show()
print('---------------')

"""
Dibujar el resultado de codificar Peppers con el diccionarios obtenido
con la imagen de Lena.

Calcular el error.
"""

peppersVec = toBlocks(peppers, len(peppers),len(peppers[0]))
flattenedPeppers = [np.ndarray.flatten(np.array(i)) for i in peppersVec]
flattenedPeppers = [[float(i) for i in row] for row in flattenedPeppers]
#kvalues son los valores de Lena
referencedPeppers,_= vq(flattenedPeppers,kvalues)
peppersVec= [np.reshape(kvalues[i],[blockSize,blockSize]) for i in referencedPeppers]
peppersVec= [[list(row)for row in block]for block in peppersVec]
recoveredPeppers = fromBlocks(peppersVec,len(peppers[0]),len(peppers))


sigma1 = np.sqrt(sum(sum((peppers-recoveredPeppers)**2))/(n*m))
print('error peppers - Lena: ' + str(sigma1))
#ratio compresion
imgSize = len(peppers[0]) * len(peppers) *pixelBits
numBlocks = len(peppers[0]) * len(peppers) / (blockSize**2)
#los valores necesitaran un numero de bits proporcional al numero de entradas
encodedImageSize =  numBlocks * math.ceil(math.log(numEntradas,2))
#un bloque a guardar por entrada, cada bloque ocupa blockSize**2 pixeles
dictSize= numEntradas * (blockSize**2) *pixelBits
recoveredImgSize = encodedImageSize + dictSize
ratio_compresion = imgSize / recoveredImgSize
print('ratio compresion peppers-lena: ' + str(ratio_compresion))
bitsxPixel= recoveredImgSize / (len(peppers[0]) * len(peppers))
print('bitsxPixel peppers-lena: ' + str(bitsxPixel))

plt.imshow(recoveredPeppers.astype(np.uint8), cmap=plt.cm.gray)
plt.show()

