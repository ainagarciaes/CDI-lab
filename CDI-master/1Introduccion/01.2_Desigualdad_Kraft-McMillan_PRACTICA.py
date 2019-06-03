# -*- coding: utf-8 -*-
"""

"""
import math
'''
Dada la lista L de longitudes de las palabras de un código 
q-ario, decidir si pueden definir un código.

'''

def  kraft1(L, q=2):
	alfa = 0.
	for qli in L:
		alfa += 1./(q**qli)
		if alfa >= 1. :
			return False
	return True


'''
Dada la lista L de longitudes de las palabras de un código 
q-ario, calcular el máximo número de palabras de longitud 
máxima, max(L), que se pueden añadir y seguir siendo un código.

'''

def  kraft2(L, q=2):
	lmax=max(L)
	alfa = 0.
	for qli in L:
		alfa += 1./(q**qli)
		if alfa >= 1. :
			return 0
	return (1. - alfa) / (1./ (q**lmax))


'''
Dada la lista L de longitudes de las palabras de un  
código q-ario, calcular el máximo número de palabras 
de longitud Ln, que se pueden añadir y seguir siendo 
un código.
'''

def  kraft3(L, Ln, q=2):
	alfa = 0.
	for qli in L:
		alfa += 1./(q**qli)
		if alfa >= 1. :
			return 0
	return math.floor((1. - alfa) / (1./ q** Ln))

'''
Dada la lista L de longitudes de las palabras de un  
código q-ario, hallar un código prefijo con palabras 
con dichas longitudes
'''

def gencandidates(old, q):
	new= []
	for x in old:
		for i in range(q):	
			new.append(x + str(i))
	return new

def Code(L,q=2):
	answer = []
	candidates = ['']
	#lo ordenamos para facilitar el crear prefijos
	L = sorted(L)
	length= 0
	for x in L:
		while length < x:
			candidates = gencandidates(candidates,q)
			length +=1
		answer.append(candidates[0])
		candidates.pop(0)
	return answer 


'''
Ejemplo
'''

L=[1,3,5,5,10,3,5,7,8,9,9,2,2,2]
L2 = [1,3,5]
L2test= [1,3]

"""ejemplos para mostrar que los kraft funcionan

print('kraft1: ' + str(kraft1(L2)))
print('kraft2: ' + str(kraft2(L2)))
print('kraft2-3: ' + str(kraft2(L2test)))
print('kraft3: ' + str(kraft3(L2,3)))

"""
print(sorted(L),' codigo final:',Code(L,3))
print(kraft1(L))
