# -*- coding: utf-8 -*-
"""

"""

import numpy as np
import scipy
import scipy.ndimage
import math
pi=math.pi
import time





import matplotlib.pyplot as plt





"""
Matrices de cuantización, estándares y otras
"""


#MODIFICADO PARA QUE QUADRE CON LOS APUNTES
Q_Luminance=np.array([
[16 ,11, 10, 16, 24, 40, 51, 61],
[12, 12, 14, 19, 26, 58, 60, 55],
[14, 13, 16, 24, 40, 57, 69, 56],
[14, 17, 22, 29, 51, 87, 80, 62],
[18, 22, 37, 56, 68, 109, 103, 77],
[24, 35, 55, 64, 81, 104, 113, 92],
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




"""
Implementar la DCT (Discrete Cosine Transform)
y su inversa para bloques NxN

dct_bloque(p,N)
idct_bloque(p,N)

p bloque NxN

"""
def inversa(x,y):
    matr = np.zeros((x,y))
    for i in range(x):
        for j in range(y):
            first= 1
            left= np.sqrt(2/x)
            right=((2*j +1)*i*pi)/ (2 * x)
            if i== 0:
                first= 1/np.sqrt(2)
            matr[i,j]=left * np.cos(right)*first
    return matr


def dct_bloque(p):
    x= len(p)
    y= len(p[0])
    C= inversa(x,y)
    bloq = np.tensordot(np.tensordot(C,p,axes=([1][0])),
                     np.transpose(C),
                     axes=([1][0]))
    return bloq

def idct_bloque(p):
    x= len(p)
    y= len(p[0])
    C= inversa(x,y)
    bloq = np.tensordot(np.tensordot(np.transpose(C),p,axes=([1][0])),
                     C,
                     axes=([1][0]))
    return bloq

"""
Reproducir los bloques base de la transformación para los casos N=4,8
Ver imágenes adjuntas.
"""

plt.figure()

N=4
i=1
while i<3:
    #1a iteracion 4, 2a iteración 8
    C = inversa(N*i,N*i)
    for row in range(i*N):
        for col in range(i*N):
            baseImage = np.tensordot(C[row], np.transpose(C[col]), 0)
            plt.imshow(baseImage)
            plt.xticks([])
            plt.yticks([])
            #plt.show()
    i+=1

"""
Funciones de ayuda para convertir a bloques y recuperar imagen
"""
#por columnas primero me facilita aplicar dct
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
    coefNulos=0
    imagen_graycopy = imagen_gray.copy()
    fil= len(imagen_gray)
    col= len(imagen_gray[0])
    imagen_jpeg = np.zeros((fil,col))
    #lo recorreremos x bloques
    for i in range(0,fil,8):
        for j in range(0,col,8):
            cur= imagen_graycopy[i:i+8,j:j+8] -128
            cur = dct_bloque(cur)
            cur= np.round(np.divide(cur,Q_Luminance))
            coefNulos += (cur == 0.).sum()
            curRecup=idct_bloque( np.multiply(cur,Q_Luminance))+128
            imagen_jpeg[i:i+8,j:j+8] = curRecup

    Sigma=np.sqrt(sum(sum((imagen_gray-imagen_jpeg)**2)))/np.sqrt(sum(sum((imagen_gray)**2)))
    print('Sigma = '+ str(Sigma))
    compressionRatio = (fil*col) / ((fil*col) - coefNulos)
    print('compressionRatio = '+ str(compressionRatio))
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

def RGBtoYCBCR(img):
    fil = len(img)
    col = len(img[0])
    ycbcr = np.zeros((fil,col,3))
    for i in range(fil):
        for j in range(col):
            [r,g,b]= img[i][j]
            ycbcr[i][j][0]= 0.299*r+0.587*g+0.114*b
            ycbcr[i][j][1]=-0.1687*r-0.3313*g+0.5*b+128
            ycbcr[i][j][2]= 0.5*r- 0.4187*g-0.0813*b+128
    return ycbcr

def YCBCRtoRGB(img):
    fil = len(img)
    col = len(img[0])
    rgb = np.zeros((fil,col,3))
    for i in range(fil):
        for j in range(col):
            [y,cb,cr]= img[i][j]
            rgb[i][j][0]= y + 1.402*(cr -128)
            rgb[i][j][1]= y - 0.71414*(cr-128) - 0.34414*(cb-128)
            rgb[i][j][2]= y + 1.772*(cb-128)
    return rgb




def jpeg_color(imagen_color):
    imagen_color_copy =imagen_color.copy()
    fil=len(imagen_color_copy)
    col=len(imagen_color_copy[0])
    #transform to Y Cb Cr
    y= np.zeros((fil,col))#luma
    cb= np.zeros((fil,col))#blue to green
    cr= np.zeros((fil,col))#red to green
    coefNulos= 0
    #cambio de espacio de colores
    ycbcr = RGBtoYCBCR(imagen_color_copy)


    imagen_jpeg = np.zeros((fil,col,3))

    for i in range(0,fil,8):
        for j in range(0,col,8):
            #cogemos cada valor y lo centramos
            bloquey = ycbcr[i:i+8,j:j+8,0] - 128
            bloquecb = ycbcr[i:i+8,j:j+8,1] - 128
            bloquecr = ycbcr[i:i+8,j:j+8,2] - 128
            #calculamos la dct y aplicamos la conversion lossy
            bloquey = np.round(np.divide(dct_bloque(bloquey),Q_Luminance))
            bloquecb = np.round(np.divide(dct_bloque(bloquecb),Q_Chrominance))
            bloquecr = np.round(np.divide(dct_bloque(bloquecr),Q_Chrominance))
            #contamos coefNulos para aproximar el ratioCompresion
            coefNulos +=(bloquey == 0.).sum()
            coefNulos +=(bloquecb == 0.).sum()
            coefNulos +=(bloquecr == 0.).sum()
            #RECUPERAR IMAGEN A PARTIR DE JPEG
            # aplicamos transform inversa y la centramos
            bloqueyRecovered = idct_bloque(np.multiply(bloquey,Q_Luminance)) +128
            bloquecbRecovered = idct_bloque(np.multiply(bloquecb,Q_Chrominance)) +128
            bloquecrRecovered = idct_bloque(np.multiply(bloquecr,Q_Chrominance)) +128
            #actualizamos nuestro bloque en la imagen
            imagen_jpeg[i:i+8,j:j+8,0] = bloqueyRecovered
            imagen_jpeg[i:i+8,j:j+8,1] = bloquecbRecovered
            imagen_jpeg[i:i+8,j:j+8,2] = bloquecrRecovered

    imagen_jpeg = YCBCRtoRGB(imagen_jpeg)
    #3 porque cada pixel tiene 3 canales
    compressionRatio = (fil*col*3) / ((fil*col*3) - coefNulos)
    print('compressionRatio = '+ str(compressionRatio))
    sigmaR =np.sqrt(sum(sum((imagen_color[:,:,0]-imagen_jpeg[:,:,0])**2)))/np.sqrt(sum(sum((imagen_color[:,:,0])**2)))
    sigmaG =np.sqrt(sum(sum((imagen_color[:,:,1]-imagen_jpeg[:,:,1])**2)))/np.sqrt(sum(sum((imagen_color[:,:,1])**2)))
    sigmaB =np.sqrt(sum(sum((imagen_color[:,:,2]-imagen_jpeg[:,:,2])**2)))/np.sqrt(sum(sum((imagen_color[:,:,2])**2)))
    Sigma=sigmaR +sigmaG +sigmaB
    print('Sigma = '+ str(Sigma))

    plt.imshow(imagen_jpeg.astype(np.uint8))
    plt.xticks([])
    plt.yticks([])
    plt.show()



    return imagen_jpeg





"""
#--------------------------------------------------------------------------
Imagen de GRISES

#--------------------------------------------------------------------------
"""


### .astype es para que lo lea como enteros de 32 bits, si no se
### pone lo lee como entero positivo sin signo de 8 bits uint8 y por ejemplo al
### restar 128 puede devolver un valor positivo mayor que 128

print('-------------IMAGEN GRISES ----------------')

mandril_gray=scipy.ndimage.imread('mandril_gray.png').astype(np.int32)

start= time.clock()
mandril_jpeg=jpeg_gris(mandril_gray)
end= time.clock()
print("tiempo",(end-start))


"""
#--------------------------------------------------------------------------
Imagen COLOR
#--------------------------------------------------------------------------
"""
## Aplico.astype pero después lo convertiré a
## uint8 para dibujar y a int64 para calcular el error

print('-------------IMAGEN COLOR ----------------')
mandril_color=scipy.misc.imread('./mandril_color.png').astype(np.int32)



start= time.clock()
mandril_jpeg=jpeg_color(mandril_color)
end= time.clock()
print("tiempo",(end-start))

