# -*- coding: utf-8 -*-

import random

'''
0. Dada una codificación R, construir un diccionario para codificar m2c y otro para decodificar c2m
'''
R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])


'''
1. Definir una función Encode(M, m2c) que, dado un mensaje M y un diccionario 
de codificación m2c, devuelva el mensaje codificado C.
'''

def Encode(M, m2c):
    C  = ""
    for i in M: 
        C += m2c[i]
    return C
    
    
''' 
2. Definir una función Decode(C, c2m) que, dado un mensaje codificado C y un diccionario 
de decodificación c2m, devuelva el mensaje original M.
'''
def Decode(C,c2m):
    M = ""
    seq= ""
    for i in C: 
        #print('hai')
        seq += i
        if seq in c2m:
            M +=c2m[seq]
            seq = ""
    return M
  

#------------------------------------------------------------------------
# Ejemplo 1
#------------------------------------------------------------------------

R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

'''
3. Generar un mensaje aleatorio M de longitud 50 con las frecuencias 
esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''
def getRandomChar():
    x = random.random()
    if x < 0.5 :
        return 'a'
    if x < 0.7:
        return 'b'
    if x < 0.85 :
        return 'c'
    if x < 0.95 :
        return 'd'
    return 'e'

orig = ""
for i in range(50):
    orig += getRandomChar()

C = Encode(orig,m2c)
M = Decode(C, c2m)
#print (M== orig)


''' 
4. Si 'a', 'b', 'c', 'd', 'e' se codifican inicialmente con un código de 
bloque de 3 bits, hallar la ratio de compresión al utilizar el nuevo código.  
'''
#los dos ultimos tienen la misma longitud
r =  3 * len(orig)/len(C)
# seguira la formula 3* / (0.5 * 1  + 0.2 * 2 + 0.15 * 3 + 0.15*4)




#------------------------------------------------------------------------
# Ejemplo 2
#------------------------------------------------------------------------
R = [('a','0'), ('b','10'), ('c','110'), ('d','1110'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
5.
Codificar y decodificar 20 mensajes aleatorios de longitudes también aleatorios.  
Comprobar si los mensajes decodificados coinciden con los originales.
'''

for i in range(20):
    length = random.randint(0,400)
    orig  = ""
    for j in range(length):
        orig += random.sample(['a','b','c','d','e'],1)[0]
    C= Encode(orig,m2c)
    M = Decode(C,c2m)
    #print ('ejercicio 5:' + str(M == orig))




#------------------------------------------------------------------------
# Ejemplo 3 
#------------------------------------------------------------------------
R = [('a','0'), ('b','01'), ('c','011'), ('d','0111'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
6. Codificar y decodificar los mensajes  'ae' y 'be'. 
Comprobar si los mensajes decodificados coinciden con los originales.
'''
 
m1= 'ae'
m2='be'
C1 = Encode(m1,m2c)
M1= Decode(C1, c2m)
C2 = Encode(m2,m2c)
M2= Decode(C2, c2m)
print ('ae ok?' + str(M1 == m1))
print ('be ok?' + str(M2 == m2))

print (str(m2) + " is different from " + str(M2) )
'''esto pasa porque al recuperar el mensaje original, tenemos varias opciones para hacerlo,
'be' queda como 011111, que se traduce a 'be' o a 'ae' con un 1 que queda suelto. 
Esto se puede solucionar añadiendo una condicion que obligue a consumir la totalidad del código y 
intente todas las combinaciones, pero complica bastante mas la traduccion.''' 
#print (C1)
#print (C2)




  




