# -*- coding: utf-8 -*-
"""
@author: martinez
"""

import math
import random

#%%
"""
Dado un mensaje y su alfabeto con sus frecuencias dar el código 
que representa el mensaje utilizando precisión infinita (reescalado)

El intervalo de trabajo será: [0,R), R=2**k, k menor entero tal que R>4T

T: suma total de frecuencias

"""

#check book
def IntegerArithmeticCode(mensaje,alfabeto,frecuencias):
	r = 1 
	T = 0
	for f in frecuencias:   # suma de freq
		T += f

	lon = 0
	while r < 4*T:          # calculo de r 
		r = 2*r
		lon += 1 #longitud de la paraula en bits

	code = ''     
	fr = '0'+str(lon)+'b'
	l = 0
	u = r-1
	scale3 = 0
	for m in mensaje:
		lfix = l
		ufix = u
		l = int(lfix + ((ufix - lfix + 1)*limiteIntervaloInf(alfabeto, frecuencias, m)/T))%r
		u = int(lfix + ((ufix - lfix + 1)*limiteIntervaloSup(alfabeto, frecuencias, m)/T) - 1)%r
		lfix = l
		ufix = u

		lbin = format(l, fr)
		ubin = format(u, fr)
		while (lbin[0] == ubin[0] or (lbin[1]=='1' and ubin[1]=='0')):
			if (lbin[0] == ubin[0]):
				code += lbin[0]                             
				l = (l*2)%r
				u = (u*2 + 1)%r
				lbin = format(l, fr)
				ubin = format(u, fr)
				while(scale3 > 0): 
					code += lbin[0]
					scale3 -= 1
			if (lbin[1]=='1' and ubin[1]=='0'):
				lbin = format(l, fr)
				ubin = format(u, fr)

				list1 = list(lbin)
				list2 = list(ubin)
				if (lbin[1] == '1'): 
					list1[1] = '0'
					l = (l*2-int(r/2))%r
				else: 
					list1[1] = '1'
					l = (l*2+int(r/2))%r

				if (ubin[1] == '1'): 
					list2[1] = '0'
					u = (u*2 + 1 - int(r/2))%r
				else: 
					list2[1] = '1'
					u = (u*2 + 1 + int(r/2))%r
				lbin = ''.join(list1)
				ubin = ''.join(list2)
				scale3 += 1
	if (scale3 > 0):
		list1 = list(lbin)
		ind = list1.index('0')
		for i in range(0, ind+1):
			code += list1[i]
		code += '1'
		for i in range(ind+1, len(lbin)):
			code += list1[i]
	else:
		code += lbin
	return code

def limiteIntervaloInf (alfabeto, frecuencias, m):
	ind = alfabeto.index(m)
	a = 0
	for i in range(0, ind):
		a += frecuencias[i]
	return a

def limiteIntervaloSup (alfabeto, frecuencias, m):
	ind = alfabeto.index(m)
	a = 0
	for i in range(0, ind+1):
		a += frecuencias[i]
	return a    

#%%
            
            
"""
Dada la representación binaria del número que representa un mensaje, la
longitud del mensaje y el alfabeto con sus frecuencias 
dar el mensaje original
"""
           
def IntegerArithmeticDecode(codigo,tamanyo_mensaje,alfabeto,frecuencias):
	r = 1 
	T = 0
	for f in frecuencias:   # suma de freq
		T += f

	lon = 0
	while r < 4*T:          # calculo de r 
		r = 2*r
		lon += 1 #longitud de la paraula en bits
	
	decoded = ''
	fr = '0'+str(lon)+'b'

	l = 0
	u = r-1  
	li = 0
	ls = lon
	t = codigo[li:ls]
	while (ls <= len(codigo) and tamanyo_mensaje > 0):
		tint = int(t, 2)
		value = int(((tint-l+1)*T-1)/(u-l+1))

		found = False
		Tant = 0
		T2 = 0
		ind = 0
		for f in frecuencias:
			T2  += f
			
			if (T2 > value and Tant <= value):
				found = True
				tamanyo_mensaje -= 1
				break
			else:
				Tant = T2
			ind += 1

		if found:
			decoded += alfabeto[ind]
			lfix = l
			ufix = u
			l = int(lfix + ((ufix - lfix + 1)*limiteIntervaloInf(alfabeto, frecuencias, alfabeto[ind])/T))%r
			u = int(lfix + ((ufix - lfix + 1)*limiteIntervaloSup(alfabeto, frecuencias, alfabeto[ind])/T) - 1)%r

			lbin = format(l, fr)
			ubin = format(u, fr)
			while (lbin[0] == ubin[0] or (lbin[1]=='1' and ubin[1]=='0')):
				if (lbin[0] == ubin[0]):                            
					l = (l*2)%r
					u = (u*2 + 1)%r
					ls += 1
					li += 1
					t = codigo[li:ls]
					tint = int(t, 2)
					lbin = format(l, fr)
					ubin = format(u, fr)
						
				if (lbin[1]=='1' and ubin[1]=='0'):
					lbin = format(l, fr)
					ubin = format(u, fr)
					ls += 1
					li += 1                                       
					t = codigo[li:ls]
					list1 = list(lbin)
					list2 = list(ubin)
					list3 = list(t)
					if (lbin[1] == '1'):                                                
						l = (l*2-int(r/2))%r
						lbin = format(l, fr)
						list1 = list(lbin)
						list1[0] = '0'
					else: 
						l = (l*2-int(r/2))%r
						lbin = format(l, fr)
						list1 = list(lbin)
						list1[0] = '1'

					if (ubin[1] == '1'):                       
						u = (u*2 + 1 - int(r/2))%r
						ubin = format(u, fr)
						list2 = list(ubin)
						list2[0] = '0'
					else:                
						u = (u*2 + 1 + int(r/2))%r
						ubin = format(u, fr)
						list2 = list(ubin)
						list2[0] = '1'


					if (t[0] == '1'):
						list3[0] = '0'
					else: 
						list3[0] = '1'
					lbin = ''.join(list1)
					ubin = ''.join(list2)
					t = ''.join(list3)
					tint = int(t, 2)   
	return decoded                                               
                
alfabeto=['1','2','3']
frecuencias=[40,1,9]
mensaje='1321'
c = IntegerArithmeticCode(mensaje,alfabeto,frecuencias)
print(c)
print(IntegerArithmeticDecode(c,len(mensaje),alfabeto,frecuencias))
#%%
'''
Definir una función que codifique un mensaje utilizando codificación aritmética con precisión infinita
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''
def tablaFrecuencias(mensaje):
	frecuencias = {}
	for i, c in enumerate(mensaje):
		if (not c in frecuencias): 
			frecuencias.update({c:1})
		else:
			num = frecuencias.get(c)
			frecuencias.update({c:num+1})
	return frecuencias


def calculaM(frecuencias):
	minima = min(frecuencias)
	m = math.ceil(-math.log2(minima))
	return m
	
def EncodeArithmetic(mensaje_a_codificar):
	f = tablaFrecuencias(mensaje_a_codificar)
	alfabeto = list(f.keys())
	frecuencias = list(f.values())

	total = sum(frecuencias)

	u = 1
	l = 0

	mensaje_codificado = ''

	for m in mensaje_a_codificar:
		laux = l
		l = laux + (u - laux)*limiteIntervaloInf(alfabeto, frecuencias, m)/total
		u = laux + (u - laux)*limiteIntervaloSup(alfabeto, frecuencias, m)/total
		while(u < 0.5 or l >= 0.5):
			if(u < 0.5):
				mensaje_codificado += '0'
				l = 2*l
				u = 2*u
			if(l >= 0.5):
				mensaje_codificado += '1'
				l = 2*(l-0.5)
				u = 2*(u-0.5)
	eos = (u+l)/2
	word_length = calculaM(frecuencias)

	tag = "{0:b}".format((int(1/eos)))

	mensaje_codificado += tag + (word_length - len(tag))*'0'
	return mensaje_codificado,alfabeto,frecuencias

def decisor(frecuencias, percentage):
	t = 0
	tnext = 0
	found = False
	i = 0
	for f in frecuencias:	
		tnext += f
		if (percentage < tnext and percentage >= t):
			found = True
			break
		t = tnext
		i += 1
	if (not found):
		i -= 1
	return i, t, tnext

def tagFloat(tag):
	res = 0.0
	for i, t in enumerate(tag):
		res += int(t)*2**-(i+1)
	return res

    
def DecodeArithmetic(mensaje_codificado,tamanyo_mensaje,alfabeto,frecuencias):
	pos = 0
	total = sum(frecuencias)
	frecuencias = [x / total for x in frecuencias]
	u = 1.0
	l = 0.0

	word_length = calculaM(frecuencias)
	mensaje_descodificado = ''
	tag = mensaje_codificado[0:word_length]
	tagfloat = tagFloat(tag)
	percentage = tagfloat / (u-l)

	while len(mensaje_descodificado) < tamanyo_mensaje:
		i, t, tnext = decisor(frecuencias, percentage)
		print(alfabeto[i], end='', flush=True)
		mensaje_descodificado += alfabeto[i]
		laux = l
		l = laux + (u - laux)*t
		u = laux + (u - laux)*tnext
		while(u < 0.5 or l >= 0.5):
			if(u < 0.5):
				pos += 1
				tag = mensaje_codificado[pos:pos+word_length]
				tagfloat = tagFloat(tag)
				l = 2*l
				u = 2*u
			if(l >= 0.5):
				pos += 1
				tag = mensaje_codificado[pos:pos+word_length]
				tagfloat = tagFloat(tag)
				l = 2*(l-0.5)
				u = 2*(u-0.5)
		percentage = (tagfloat - l) / (u-l)
	return mensaje_descodificado
        
#%%
'''
Ejemplo (!El mismo mensaje se puede codificar con varios códigos¡)

'''
'''
lista_C=['010001110110000000001000000111111000000100010000000000001100000010001111001100001000000',
         '01000111011000000000100000011111100000010001000000000000110000001000111100110000100000000']
alfabeto=['a','b','c','d']
frecuencias=[1,10,20,300]
mensaje='dddcabccacabadac'
tamanyo_mensaje=len(mensaje)  

for C in lista_C:
    mensaje_recuperado=DecodeArithmetic(C,tamanyo_mensaje,alfabeto,frecuencias)
    print(mensaje==mensaje_recuperado)



#%%

'''
#Ejemplo



mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
mensaje_codificado,alfabeto,frecuencias=EncodeArithmetic(mensaje)
mensaje_recuperado=DecodeArithmetic(mensaje_codificado,len(mensaje),alfabeto,frecuencias)

ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
print(ratio_compresion)

if (mensaje!=mensaje_recuperado):
        print('!!!!!!!!!!!!!!  ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        
