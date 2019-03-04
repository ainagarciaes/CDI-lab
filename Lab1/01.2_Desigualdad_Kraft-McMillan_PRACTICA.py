# -*- coding: utf-8 -*-
"""

"""

import queue

'''
Dada la lista L de longitudes de las palabras de un código 
q-ario, decidir si pueden definir un código.

'''

def  kraft1(L, q=2):
    sum = 0.0
    for l in L:
        sum += (1/q)**l
    if (sum <= 1): 
        return True
    else:
        return False


'''
Dada la lista L de longitudes de las palabras de un código 
q-ario, calcular el máximo número de palabras de longitud 
máxima, max(L), que se pueden añadir y seguir siendo un código.

'''

def  kraft2(L, q=2):
    sum = 0.0
    for l in L:
        sum += (1/q)**l

    n = (1-sum)*q**max(L)
    return int(n)
    

'''
Dada la lista L de longitudes de las palabras de un  
código q-ario, calcular el máximo número de palabras 
de longitud Ln, que se pueden añadir y seguir siendo 
un código.
'''

def  kraft3(L, Ln, q=2):
    sum = 0.0
    for l in L:
        sum += (1/q)**l

    n = (1-sum)*q**Ln
    return int(n)

'''
Dada la lista L de longitudes de las palabras de un  
código q-ario, hallar un código prefijo con palabras 
con dichas longitudes
'''
def Code(L,q=2):
    L = sorted(L)
    q1 = queue.Queue(0)
    longQ = 1

    i = 0
    while i < q:
        q1.put(str(i))  #queue init
        i += 1

    code = []

    for l in L:
        while l != longQ:               #increase longQ until it matches the required lenght by l
            longQ += 1
            q2 = queue.Queue(0) 
            while not q1.empty():       #transfer content of q to q2
                q2.put(q1.get())
            while not q2.empty():       #empty q2 adding its content +k to q thus obtaining longQ+1 combinations
                aux = q2.get()
                i = 0
                while i < q:
                    q1.put(aux+str(i))
                    i += 1
        code.append(q1.get())           #get the required code of lenght l and proceed to process l+1
    return code

'''
Ejemplos
'''

L=[2,3,3,3,4,4,4,6] 
q=2

print("\n",sorted(L),' codigo final:',Code(L,q))
print(kraft1(L,q))
print(kraft2(L,q))
print(kraft3(L,max(L)+1,q))

q=3
L=[1,3,5,5,3,5,7,2,2,2]
print(sorted(L),' codigo final:',Code(L,q))
print(kraft1(L,q))

