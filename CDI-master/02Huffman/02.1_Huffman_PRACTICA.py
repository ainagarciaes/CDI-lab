# -*- coding: utf-8 -*-
"""

"""

import math
from collections import defaultdict


#%%----------------------------------------------------

'''
Dada una distribucion de probabilidad, hallar un código de Huffman asociado
'''


def Code(tree):
	#expresiones mas cortas
	add0 = lambda x:['0' + x[0]]+ x[1:]
	add1 = lambda x:['1' + x[0]]+ x[1:]
	if isinstance(tree[0],list) and isinstance(tree[1],list): #hay que crecer por la izquierda y derecha
		#print(1)
		return list(map(add0,Code(tree[0]))) + list(map(add1,Code(tree[1])))
	if isinstance(tree[0],list) : #crece por la izquierda solo
		#print(2)
		return list(map(add0,Code(tree[0])))+[['1',tree[1]]]
	if isinstance(tree[1],list):#crece por la derecha solo
		#print(3)
		return [['0',tree[0]]]+list(map(add1,Code(tree[1])))
	#print(4)
	return [['0',tree[0]],['1',tree[1]]]#no crece mas	
	
	 

def Huffman(p):
	q= []
	i = 0
	#preparando nodos
	while i < len(p):
		q.append([p[i],i])
		i+=1
	#uniendo nodos en arbol
	while len(q) > 1:
		q = sorted(q, key= lambda elem : elem[0])
		q =[[q[0][0]+ q[1][0]]+ [[q[0][1],q[1][1]] ]] + q[2:]	
	#ahora deconstruimos el arbol y vamos asignando el código
	q = q[0][1]#solo nos interesa la parte derecha
	codigo= Code(q)
	codigo.sort(key = lambda x: x[1])
	for i in range(len(p)):
		codigo[i][1]=p[i]
	return codigo


#%%----------------------------------------------------

'''
Dada la ddp p=[0.80,0.1,0.05,0.05], hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

p=[0.80,0.1,0.05,0.05]

print(Huffman(p))
#%%----------------------------------------------------

'''
Dada la ddp p=[1/n,..../1/n] con n=2**8, hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

n=2**8
p=[1/n for _ in range(n)]

encode = Huffman(p)
sumlen=0
entropia=0
for code,prob in encode:
	sumlen+=len(code)
	entropia +=prob* math.log2(1./prob)
longmedia=sumlen/len(encode)
print (longmedia)
print (entropia)
print('Tiene sentido que esto nos pase, pues estamos usando potencias de 2, esto hace que Huffman sea optimo')

#%%----------------------------------------------------

'''
Dado un mensaje hallar la tabla de frecuencia de los caracteres que lo componen
'''
def tablaFrecuencias(mensaje):
	mychars=defaultdict(lambda:0)
	for i in mensaje:
	#por caracter
		mychars[i]+=1
	return mychars

'''
Definir una función que codifique un mensaje utilizando un código de Huffman 
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''
#%%----------------------------------------------------

def EncodeHuffman(mensaje_a_codificar):
	tabla =tablaFrecuencias(mensaje_a_codificar)
	tabla= [[x,tabla[x]] for x in tabla ] 
	#modulo unitario	
	temp = 0 
	for x,y in tabla:
		temp +=y
	tabla = [[x[0],x[1]/temp] for x in tabla]
	tabla = sorted(tabla)
	#print(tabla) #debug
	freq = [x[1] for x in tabla]
	codificacion= Huffman(freq)
	#print(codificacion)
	m2c = list(zip(tabla,codificacion))
	m2c= dict([(x[0],y[0] ) for (x,y) in m2c])
	#print(m2c)
	mensaje_codificado=''
	for char in mensaje_a_codificar:
		mensaje_codificado += m2c[char]
	return mensaje_codificado, m2c
    
    

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
  

def DecodeHuffman(mensaje_codificado,m2c):
	c2m = dict([(m2c[x], x) for x in list(m2c)])
	
	return Decode(mensaje_codificado,c2m)
        
#%%----------------------------------------------------

'''
Ejemplo
'''
mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
mensaje_codificado, m2c=EncodeHuffman(mensaje)
mensaje_recuperado=DecodeHuffman(mensaje_codificado,m2c)
print(mensaje_recuperado)
ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
print(ratio_compresion)

'''
Si tenemos en cuenta la memoria necesaria para almacenar el diccionario, 
¿cuál es la ratio de compresión?
'''

