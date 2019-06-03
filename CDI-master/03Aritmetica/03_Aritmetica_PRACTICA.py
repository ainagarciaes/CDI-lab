# -*- coding: utf-8 -*-


import math
import random

"""
Dado x en [0,1) dar su representacion en binario, por ejemplo
dec2bin(0.625)='101'
dec2bin(0.0625)='0001'

Dada la representación binaria de un real perteneciente al intervalo [0,1)
dar su representación en decimal, por ejemplo

bin2dec('101')=0.625
bin2dec('0001')=0.0625

nb número máximo de bits

"""


def dec2bin(x,nb=100):
	ans=''
	interv= 1.0
	while nb >= len(ans) and x != 0:
		interv/=2
		if x >= interv:
			ans+= '1'
			x-=interv
		else :
			ans+= '0'
	return ans


def bin2dec(xb):
	ans= 0.0
	interv= 1.0
	for i in xb:
		if i == '1':
			ans+=interv/2.
		interv/=2.0
	return ans

#print(bin2dec('101'))#0.625
#print(bin2dec('0001'))#0.0625
#print(dec2bin(0.625))#101
#print(dec2bin(0.0625))#0001

"""
Dada una distribución de probabilidad p(i), i=1..n,
hallar su función distribución:
f(0)=0
f(i)=sum(p(k),k=1..i).
"""

def cdf(p):
	i=0
	q=[0.]
	while i< len(p):
		q.append( q[i] + p[i])
		i +=1
	return q
"""
print('CDF')
probabilidades=[0.4,0.3,0.2,0.1]
print(probabilidades)
mycdf= cdf(probabilidades)
print(probabilidades)
print(mycdf)
print('----------------')
"""
"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el intervalo (l,u) que representa al mensaje.

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
Arithmetic(mensaje,alfabeto,probabilidades)=0.876 0.8776
"""

def Arithmetic(mensaje,alfabeto,probabilidades):
	distr=cdf(probabilidades)
	i=1
	limInf=distr[alfabeto.index(mensaje[0])]
	limSup=distr[alfabeto.index(mensaje[0])+1]
	while i < len(mensaje) :
		infOld=limInf
		supOld=limSup
		cur=alfabeto.index(mensaje[i])
		probdown=distr[cur]
		probup=distr[cur+1]
		limInf=infOld+(supOld-infOld)*probdown
		limSup=infOld+(supOld-infOld)*probup

		i+=1
	return limInf,limSup

"""
print('Arithmetic')
mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
ans= Arithmetic(mensaje,alfabeto,probabilidades)
print(ans[0])
print(ans[1])
print(ans)
print('------------------')

"""

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar la representación binaria de x/2**(t) siendo t el menor
entero tal que 1/2**(t)<M-m, x entero (si es posible par) tal
que m*2**(t)<= x <M*2**(t)

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
EncodeArithmetic1(mensaje,alfabeto,probabilidades)='111000001'
"""

def EncodeArithmetic1(mensaje,alfabeto,probabilidades):
	(m,M) = Arithmetic(mensaje,alfabeto,probabilidades)
	interv= M-m
	t=1
	#encontrar precisión necesaria
	while 1./(2**t) > interv :
		t+=1.
	xmin= math.ceil(m*(2**t))
	xmax= math.floor(M*(2**t))
	if xmin % 2 ==0:
		return bin(int(xmin/2))[2:]
	if xmax % 2  == 0:
		return bin(int(xmax/2))[2:]
	return bin(int(xmin))[2:]


print('Arithmetic1')
mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
ans= EncodeArithmetic1(mensaje,alfabeto,probabilidades)
print(ans)
print('------------------')

"""
Dado un mensaje y su alfabeto con su distribución de probabilidad
dar el código que representa el mensaje obtenido a partir de la
representación binaria de M y m

mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
EncodeArithmetic2(mensaje,alfabeto,probabilidades)='111000001'

"""

def EncodeArithmetic2(mensaje,alfabeto,probabilidades):
	(m,M) = Arithmetic(mensaje,alfabeto,probabilidades)
	m= dec2bin(m)
	M= dec2bin(M)
	i=0
	while i < len(m) and i < len(M):
		if m[i] != M[i] :
			while m[i]==1:
				i+=1
			return m[0:i]+'1'
		i+=1

	return m[0:i]



print('Arithmetic2')
mensaje='ccda'
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
ans= EncodeArithmetic2(mensaje,alfabeto,probabilidades)
print(ans)
print('------------------')



"""
Dada la representación binaria del número que representa un mensaje, la
longitud del mensaje y el alfabeto con su distribución de probabilidad
dar el mensaje original

code='0'
longitud=4
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
DecodeArithmetic(code,longitud,alfabeto,probabilidades)='aaaa'

code='111000001'
DecodeArithmetic(code,4,alfabeto,probabilidades)='ccda'
DecodeArithmetic(code,5,alfabeto,probabilidades)='ccdab'

"""

def DecodeArithmetic(code,n,alfabeto,probabilidades):
	mensajedec=bin2dec(code)
	mycdf= cdf(probabilidades)
	mensajealf=''
	while n > 0:
		n+=-1
		i=0
		while mycdf[i] < mensajedec:
			i+=1
		mensajealf+= alfabeto[i-1]
		mensajedec = (mensajedec - mycdf[i-1])/(mycdf[i]-mycdf[i-1])
	return mensajealf

"""
print('DecodeArithmetic')
code='0'
longitud=4
alfabeto=['a','b','c','d']
probabilidades=[0.4,0.3,0.2,0.1]
ans=DecodeArithmetic(code,longitud,alfabeto,probabilidades)
print('aaaa == ' + ans)

print('-------')
code='111000001'
ans2 = DecodeArithmetic(code,4,alfabeto,probabilidades)
print('ccda == ' + ans2)
ans2 = DecodeArithmetic(code,5,alfabeto,probabilidades)
print('ccdab == ' +ans2)

print('-------')
"""


'''
Función que compara la longitud esperada del
mensaje con la obtenida con la codificación aritmética
'''

def comparacion(mensaje,alfabeto,probabilidades):
	p=1.
	indice=dict([(alfabeto[i],i+1) for i in range(len(alfabeto))])
	for i in range(len(mensaje)):
		p=p*probabilidades[indice[mensaje[i]]-1]
	aux=-math.log(p,2), len(EncodeArithmetic1(mensaje,alfabeto,probabilidades)), len(EncodeArithmetic2(mensaje,alfabeto,probabilidades))
	
	print('Información y longitudes:',aux)
	return aux


'''
Generar 10 mensajes aleatorios de longitud 10<=n<=20 aleatoria
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e', codificarlo y compararlas longitudes
esperadas con las obtenidas.
'''

alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
    Y = []
    for _ in range(k):
        Y +=[random.choice(X)]
    return Y

l_max=20

for _ in range(10):
    n=random.randint(10,l_max)
    L = rd_choice(U, n)
    mensaje = ''
    for x in L:
        mensaje += x
    print('---------- ',mensaje)
    C=comparacion(mensaje,alfabeto,probabilidades)




'''
Generar 10 mensajes aleatorios de longitud 10<=n<=100 aleatoria
con las frecuencias esperadas 50, 20, 15, 10 y 5 para los caracteres
'a', 'b', 'c', 'd', 'e' y codificarlo.
'''
alfabeto=['a','b','c','d','e']
probabilidades=[0.5,0.2,0.15,0.1,.05]
U = 50*'a'+20*'b'+15*'c'+10*'d'+5*'e'
def rd_choice(X,k = 1):
    Y = []
    for _ in range(k):
        Y +=[random.choice(X)]
    return Y

l_max=100

for _ in range(10):
    n=random.randint(10,l_max)
    L = rd_choice(U, n)
    mensaje = ''
    for x in L:
        mensaje += x
    print('---------- ',mensaje)
    C = EncodeArithmetic1(mensaje,alfabeto,probabilidades)
    print(C)
