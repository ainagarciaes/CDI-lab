# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import time
import scipy
import scipy.ndimage
import math 
pi=math.pi




import matplotlib.pyplot as plt
     
"""
Matrices de cuantización, estándares y otras
"""

    
Q_Luminance=np.array([
[16 ,11, 10, 16,  24,  40,  51,  61],
[12, 12, 14, 19,  26,  58,  60,  55],
[14, 13, 16, 24,  40,  57,  69,  56],
[14, 17, 22, 29,  51,  87,  80,  62],
[18, 22, 37, 56,  68, 109, 103,  77],
[24, 35, 55, 64,  81, 104, 113,  92],
[49, 64, 78, 87, 103, 121, 120, 101],
[72, 92, 95, 98, 112, 100, 103, 99]])

Q_Chrominance=np.array([
[17, 18, 24, 47, 99, 99, 99, 99],
[18, 21, 26, 66, 99, 99, 99, 99],
[24, 26, 56, 99, 99, 99, 99, 99],
[47, 66, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99],
[99, 99, 99, 99, 99, 99, 99, 99]])

def Q_matrix(r=1):
    m=np.zeros((8,8))
    for i in range(8):
        for j in range(8):
            m[i,j]=(1+i+j)*r
    return m

"""
Implementar la DCT (Discrete Cosine Transform) 
y su inversa para bloques NxN

dct_bloque(p,N)
idct_bloque(p,N)

p bloque NxN

"""

def transformacio(x, y):
    tr = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            a = np.sqrt(2/x)
            b = ((2*j+1)*i*pi)/(2*x)
            c = 1
            if i == 0:
                c = 1/np.sqrt(2)
            tr[i,j] = a*np.cos(b)*c
    return tr

def dct_bloque(p):
    x, y = p.shape
    inv = transformacio(x,y)
    res = np.tensordot(np.tensordot(inv, p, axes=([1][0])), np.transpose(inv) ,axes=([1][0]))
    return res
    
def idct_bloque(p):
    x, y = p.shape
    inv = transformacio(x, y)
    res = np.tensordot(np.tensordot(np.transpose(inv), p ,axes=([1][0])), inv, axes=([1][0]))
    return res

"""
Reproducir los bloques base de la transformación para los casos N=4,8
Ver imágenes adjuntas.
"""

def printBlocks(N):
    inv = transformacio(N,N)
    i = 0
    for row in range(N):
        for col in range(N):
            i += 1
            plt.subplot(N, N, i)
            baseImage = np.tensordot(inv[row], np.transpose(inv[col]), 0)
            plt.imshow(baseImage)
            plt.xticks([])
            plt.yticks([])
    plt.show()
    return

printBlocks(4)
printBlocks(8)

"""
Implementar la función jpeg_gris(imagen_gray) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen de grises 'imagen_gray' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error
Sigma=np.sqrt(sum(sum((imagen_gray-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_gray)**2)))


"""

def jpeg_gris(imagen_gray):
    #adapto la imagen a mi funcion
    nuls=0
    rows, cols = np.shape(imagen_gray)
    imagen_jpeg = np.zeros((rows,cols))

    for i in range(0,rows,8):
        for j in range(0,cols,8):
            c = np.round(np.divide(dct_bloque(imagen_gray[i:i+8, j:j+8] - 128), Q_Luminance))
            nuls += (c == 0.).sum()
            recuperada = idct_bloque(np.multiply(c, Q_Luminance)) + 128
            imagen_jpeg[i:i+8, j:j+8] = recuperada

    sigma=np.sqrt(sum(sum((imagen_gray-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_gray)**2)))
    print('sigma: ', sigma)

    ratio = (rows*cols) / ((rows*cols) - nuls)
    print('ratio: ', ratio)

    plt.imshow(imagen_jpeg, cmap=plt.cm.gray)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    return imagen_jpeg

"""
Implementar la función jpeg_color(imagen_color) que: 
1. dibuje el resultado de aplicar la DCT y la cuantización 
(y sus inversas) a la imagen RGB 'imagen_color' 

2. haga una estimación de la ratio de compresión
según los coeficientes nulos de la transformación: 
(#coeficientes/#coeficientes no nulos).

3. haga una estimación del error para cada una de las componentes RGB
Sigma=np.sqrt(sum(sum((imagen_color-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_color)**2)))

"""

def rgb2ycbcr(img):
    rows, cols, _ = np.shape(img)
    ycbcr = np.zeros((rows,cols,3))
    for i in range(rows):
        for j in range(cols):
            [r,g,b]= img[i][j]
            ycbcr[i][j][0]= 0.299*r+0.587*g+0.114*b
            ycbcr[i][j][1]=-0.1687*r-0.3313*g+0.5*b+128
            ycbcr[i][j][2]= 0.5*r- 0.4187*g-0.0813*b+128
    return ycbcr

def ycbcr2rgb(img):
    rows, cols, _ = np.shape(img)
    rgb = np.zeros((rows,cols,3))
    for i in range(rows):
        for j in range(cols):
            [y,cb,cr]= img[i][j]
            rgb[i][j][0]= y + 1.402*(cr -128)
            rgb[i][j][1]= y - 0.71414*(cr-128) - 0.34414*(cb-128)
            rgb[i][j][2]= y + 1.772*(cb-128)
    return rgb

def jpeg_color(imagen_color):
    # parametres utils
    rows, cols, _ = np.shape(imagen_color) # mida de la imatge
    nuls = 0 # suma dels coef nuls
    ycbcr = rgb2ycbcr(imagen_color)

    imatgeRecuperada = np.zeros((rows, cols, 3)) #imatge recuperada en YCBCR
    for i in range(0, rows, 8):
        for j in range(0, cols, 8):
            # conversio
            by = np.round(np.divide(dct_bloque(ycbcr[i:i+8, j:j+8, 0] - 128), Q_Luminance))
            bcb = np.round(np.divide(dct_bloque(ycbcr[i:i+8, j:j+8, 1] - 128), Q_Chrominance))
            bcr = np.round(np.divide(dct_bloque(ycbcr[i:i+8, j:j+8, 2] - 128), Q_Chrominance))
            # coef
            nuls += (by == 0.).sum()
            nuls += (bcb == 0.).sum() 
            nuls += (bcr == 0.).sum()
            # recuperacio
            imatgeRecuperada[i:i+8, j:j+8, 0] = idct_bloque(np.multiply(by, Q_Luminance)) + 128
            imatgeRecuperada[i:i+8, j:j+8, 1] = idct_bloque(np.multiply(bcb, Q_Chrominance)) + 128
            imatgeRecuperada[i:i+8, j:j+8, 2] = idct_bloque(np.multiply(bcr, Q_Chrominance)) + 128
    print(nuls)

    rgb = ycbcr2rgb(imatgeRecuperada)
    plt.imshow(rgb/255) 
    plt.xticks([])
    plt.yticks([])
    plt.show() 

    ratio = (rows*cols*3)/(rows*cols*3-nuls)
    print('ratio:', ratio)
    sigma = np.sqrt(sum(sum((imagen_color-imatgeRecuperada)**2)))/np.sqrt(sum(sum((imagen_color)**2)))
    print('sigma:', sigma)
    return rgb
"""
#--------------------------------------------------------------------------
Imagen de GRISES

#--------------------------------------------------------------------------
"""

### .astype es para que lo lea como enteros de 32 bits, si no se
### pone lo lee como entero positivo sin signo de 8 bits uint8 y por ejemplo al 
### restar 128 puede devolver un valor positivo mayor que 128

#mandril_gray=plt.imread('mandril_gray.png').astype(np.int32)
mg = plt.imread('mandril_gray.png')
mg_int = np.array(mg) * 255


start= time.clock()
mandril_jpeg=jpeg_gris(mg_int)
end= time.clock()
print("tiempo",(end-start))

"""
#--------------------------------------------------------------------------
Imagen COLOR
#--------------------------------------------------------------------------
"""
## Aplico.astype pero después lo convertiré a 
## uint8 para dibujar y a int64 para calcular el error

#mandril_color=plt.imread('mandril_color.png').astype(np.int32)
mc = plt.imread('mandril_color.png')
mc_int = np.array(mc) * 255

start= time.clock()
mandril_jpeg=jpeg_color(mc_int)     
end= time.clock()
print("tiempo",(end-start))








