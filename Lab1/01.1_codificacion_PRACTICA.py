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
    C = ''
    for m in M:
        C += m2c[m]
    return C
    
    
''' 
2. Definir una función Decode(C, c2m) que, dado un mensaje codificado C y un diccionario 
de decodificación c2m, devuelva el mensaje original M.
'''
def Decode(C,c2m):
    M = ''
    code = ''
    for c in C:
        code += c
        if (code in c2m):
            M += c2m[code]
            code = ''
    return M
  

#------------------------------------------------------------------------
# Ejemplo 1
#------------------------------------------------------------------------

R = [('a','0'), ('b','11'), ('c','100'), ('d','1010'), ('e','1011')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])


#------------------------------------------------------------------------
# Ejemplo 2
#------------------------------------------------------------------------
R = [('a','0'), ('b','10'), ('c','110'), ('d','1110'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
3.
Codificar y decodificar 20 mensajes aleatorios de longitudes también aleatorias.  
Comprobar si los mensajes decodificados coinciden con los originales.
'''

for x in range (0, 20):
    num = random.randint(0,50)
    m = ''
    for d in range (0, num):
        m += random.choice('abcde')
    print(str(x+1) + ":")
    print("M: " + m)
    enc = Encode(m, m2c)
    dec = Decode(enc, c2m)
    print("D: " + dec)
        





#------------------------------------------------------------------------
# Ejemplo 3 
#------------------------------------------------------------------------
R = [('a','0'), ('b','01'), ('c','011'), ('d','0111'), ('e','1111')]

# encoding dictionary
m2c = dict(R)

# decoding dictionary
c2m = dict([(c,m) for m, c in R])

''' 
4. Codificar y decodificar los mensajes  'ae' y 'be'. 
Comprobar si los mensajes decodificados coinciden con los originales.
'''

ae = Encode('ae', m2c)
be = Encode('be', m2c)
aed = Decode(ae, c2m)
bed = Decode(be, c2m)

print("'ae' encoded is " + ae + " and decoded is " + aed)
print("'be' encoded is " + be + " and decoded is " + bed)


'''
¿Por qué da error? 

Porque el codigo de 'a' es prefijo del codigo de 'b'

(No es necesario volver a implementar Decode(C, m2c) para que no dé error)
'''



  




