# -*- coding: utf-8 -*-
"""
"""
import sys
import math

#%%----------------------------------------------------

class HNode(object):
    def __init__(self, root, left, right, code, value):
        self.root = root #string w/ the sum of probabilities/frequency of the subnodes
        self.value = value
        self.left = left #HNode
        self.right = right #HNode
        self.code = code #Huffman code

'''
Dada una distribucion de probabilidad, hallar un código de Huffman asociado
'''

def assignCodes(tree): #tree is a root node
    if (tree.left is not None): 
        tree.left.code = "0"
        assignCodes(tree.left)
    
    if (tree.right is not None): 
        tree.right.code= "1"
        assignCodes(tree.right)
    return

def printCodes(tree, code):
    if (tree.left is None): # if its a leaf
        #print("Freq: " + str(tree.root) + " Code: " + code + "" + tree.code + " Value: " + str(tree.value))
        return [code + tree.code]
    else: 
        return printCodes(tree.left, code + tree.code) + printCodes(tree.right, code + tree.code)

def createTree(p):
    tree = []
    i = 0
    for P in p:
        n = HNode(P, None, None, "", i)
        i += 1
        tree.append(n)

    tree = sorted(tree, key=lambda x: x.root)
    while (len(tree) > 1):
        n = HNode(tree[0].root+tree[1].root, tree[1], tree[0], "", "")
        tree.pop(1)
        tree.pop(0)
        tree.append(n)
        tree = sorted(tree, key=lambda x: x.root)
    return tree[0]

def Huffman(p):
    tree = createTree(p) #root node of the huffmann tree, no codes assigned yet
    assignCodes(tree)
    return printCodes(tree, "")


#
p=[0.5,0.1,0.2,0.1,0.05,0.05]
s=Huffman(p)

#print(s)
'''
p=[0.5,0.1,0.2,0.1,0.05,0.05]

Huffman(p)=['1', '0101', '00', '011', '01000', '01001'] (¡NO ES ÚNICO!)
'''

#%%----------------------------------------------------

'''
Dada la ddp p=[1/n,....,1/n] con n=2**8, hallar un código de Huffman asociado,
la entropía de p y la longitud media de código de Huffman hallado.
'''

n=2**8
p=[1/n for _ in range(n)]

entropia = 0

s = Huffman(p)
for P in p:
    entropia -= P*math.log2(P) 

'''
ENTROPIA:
como son equiprobables: (funcion de distribucion uniforme)
entropia = n * -(P * log2(P))
entropia = 1 * (-log2(1/n))
entropia = log2(n) = log2(2**8) = 8 * log2(2) = 8
'''

'''
LONGITUDMEDIA:
longitudmedia: sum(len(s[i])*p(i)) 
como es equiprobable:   len(s[i]) = k
                        p(i) = k2 -> suma de todas = 1
k * 1 -> k = 8 = (log2(n))

'''
#print(s)
#print(entropia)

# TODO longitud media

#%%----------------------------------------------------

'''
Dado un mensaje hallar la tabla de frecuencia de los caracteres que lo componen
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
    

#mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
#print(tablaFrecuencias(mensaje))

"""
Ejemplo

mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'

tablaFrecuencias(mensaje)=
[[' ', 381], [',', 46], ['.', 8], [';', 3], ['B', 1], ['C', 2], ['E', 2], ['L', 3], ['N', 1], ['S', 2], ['V', 1], ['a', 267], ['b', 46], ['c', 64], ['d', 104], ['e', 238], ['f', 6], ['g', 23], ['h', 15], ['i', 98], ['j', 7], ['l', 112], ['m', 49], ['n', 111], ['o', 141], ['p', 48], ['q', 25], ['r', 126], ['s', 145], ['t', 68], ['u', 87], ['v', 11], ['x', 1], ['y', 30], ['z', 11], ['á', 11], ['é', 3], ['í', 12], ['ñ', 4], ['ó', 5], ['ú', 1]]
"""

#%%----------------------------------------------------
'''
Definir una función que codifique un mensaje utilizando un código de Huffman 
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''

def getCodification(tree, code):
    if (tree.left is None): # if it is a leaf
        k = tree.value
        v = code + tree.code
        return {k:v}
    else: 
        x = getCodification(tree.left, code + tree.code)
        y = getCodification(tree.right, code + tree.code)
        x.update(y)
        return x

def createTree2(freq):
    tree = []
    for k in freq.keys():
        n = HNode(freq.get(k), None, None, "", k)
        tree.append(n)

    tree = sorted(tree, key=lambda x: x.root)
    while (len(tree) > 1):
        n = HNode(tree[0].root+tree[1].root, tree[1], tree[0], "", "")
        tree.pop(1)
        tree.pop(0)
        tree.append(n)
        tree = sorted(tree, key=lambda x: x.root)
    return tree[0]

def Huffman2(freq):
    tree = createTree2(freq) #root node of the huffmann tree, no codes assigned yet
    assignCodes(tree)
    return getCodification(tree, "")

def EncodeHuffman(mensaje_a_codificar):
    t = tablaFrecuencias(mensaje_a_codificar)
    m2c = Huffman2(t)
    
    mensaje_codificado = ''
    for i, c in enumerate(mensaje):
        mensaje_codificado += m2c.get(c)

    return mensaje_codificado, m2c
    
    
def DecodeHuffman(mensaje_codificado,m2c):
    c2m = {v: k for k, v in m2c.items()}

    mensaje_decodificado = ''
    code = ''
    for c in mensaje_codificado:
        code += c
        if (code in c2m):
            mensaje_decodificado += c2m.get(code)
            code = ''
    return mensaje_decodificado
        
mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'

m, m2c = EncodeHuffman(mensaje)
#print(m)
#print(DecodeHuffman(m, m2c))

"""
Ejemplo

mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'

mensaje_codificado, m2c=EncodeHuffman(mensaje)

¡ATENCIÓN: m NO ES ÚNICO!
m2c={'o': '110', 'v': '11011101', 'c': '11111', 'j': '00001110', ';': '1011011101', 'u': '11010', 'V': '101101110011', 'r': '0010', 'b': '101110', 'á': '11011001', 'E': '1101111111', 'x': '101101110010', 'g': '1101101', 's': '1100', 'S': '1101111110', 'ó': '110111001', 'e': '011', 'B': '11011111000', 'm': '00000', 'l': '0011', ',': '101111', 'z': '11011000', ' ': '100', 'd': '10101', 'p': '101100', 'L': '1011011111', 'í': '10110110', 'C': '1101111101', 'q': '1011010', 'N': '11011111001', '.': '11011110', 'i': '10100', 'a': '010', 'y': '000010', 'ñ': '110111000', 'ú': '10110111000', 't': '11110', 'h': '0000110', 'é': '1011011110', 'n': '0001', 'f': '00001111'}
mensaje_codificado='101101111101010000001100110010111010100111110101001111110100110101010101010101100101011110001000000101101100101000011010100110010100011110011110010110111101001101111111001110011011101101000110001111101110100110111111011010001010111110011111010001110100011000111110011100000010100101100011001001111011000111011001110101111100011000001011001101000001110010101110010100001101011001000001110101011100111100100101110001101000011011010110100111111110100000101011001001011010110100111001100011100001001011001101101010101110010000110001000111001111111100010001001100101000000110010111111010001010001100111001101111100111100010111100111101111010011011111110001100001101011001001111101000110011011110010000011110100000011001010111010110110010100000001101100111001000010110101010010101111010010110101101001110001100111000010110100000011100010100011110011110001010100101010110001111100111001010101110000111110110010000100110000011100011101000001111011001001010101110010110011100011110111011110101111100111100010010101100111011001011111001011000100000111001011001000000101001011000101011000110011011110010010110101101001110010100101110010000110010101011100010001000101110000010111010001100011000100010001011100000101110101111100101010111000101111101100100101000110001100010111110110010010101111100101010111000111100101101011010101000001010100011000110001111001011010110101010000010101000010011110111011110001101000011010111101000000101001011000110010110010100110110111010101001011011110000110101111011000111011111001111111100000011101000000001000101010010110011101100010110010010110101101001110011000111001011101101011001111101000011000000101000000110110100000100110001100000010100101101011010011100011001110001010100001001110001100011101110111010011001111011101011100011000110011001101011001001011000011101000111101101110100111100100101000001110111011010011001010010111000110111100110111101001101111101110100100011100111101101000101011100101100100101010111001011001010000110011110100110011111011001011111000101011010110100110011001101011001000000010100110110101000001110010110010010101011100001101010010111001011001101000100101011111000101011010110100110011001101011001001100111010111000100101100100101010111001111011101010111101001100011100000011101101000011111001010111001000011000110001100110100001100000001110000111110110111001000110111110010110001000101101100110111001000011100011100111111110000001110100101011110001000000101001010101011001001101000011000000011100000001100011111011101000000101001011100010101000001111110101011100100001100101010111000001110100111101110111101001100111010111000100111100010001111110010101010101100101111100101011010011001011000110010110011011001000110101111011000111011111001111000100111011000100001101011110100110100001010110010010110011100010100001101011001001011000100010011101010111100100000011001011001111001010000111110110010011111001010100110011110010001101111001001111001100000101110001111100010111011001110110010010101011100001111101100100000011110100010111000110111100101111100111011110001001011001000000110010110011110010100001111101100100111110100010111100110011011110010010101011100101100010101100011001110000000010001110010110001111011010101010111101000101000011010110010001111001011010110101010000010101100101111100000010100000011001010111010110110010100101100001111010000000101001011010110100111000011001101111011010101011100101000101001101000011001111001100101111101100101001011001010011001110101111100000010100010001001100011010000110011010100101101011010011100110001110010100000111111001011010110011110010101110010100101100010001001010010101101101100101100101111100111010010110001000100101000101101110001110110010111110001100011000011010100110111011010010101001010100011001001010010101011100110100001100011110011111010101100010001001011110011101111100010110110101000100010010101010101000101001101000011001011000011111000000111011011110100101101110011011111101101011001111001010111110000110101000000011010000010100000111101011100011011100000010100001101101000111001111110100110101010101010101101111100111111110001011110011100011000110000110110000111001000011110100110010100110110100111110101111100000011001011111101101100101000011010100101011010011011010111100111101010011011100100011001010101100111001111111101111110100101011110100000010100101010111000011010100111000110011010100101100111010101001010100101010101011111000000101001010101111001111101000011100010101110010100111000001001100011010111101000110001111100010011100110011010011110111000111011001000110011100000001110000111011100111110111000011110100000010100000011110100000010100001110100010001010011011000110100000010111010100101011110100101010111000011010100111110100000010110001000010101001010101110011111111000101110101111100101101011010011100001001111110110100000010111001010111001010001000110011110110011000110001100001111101000100011111101110100101010111000011010100011110010111001100111111001011110111000100010011100011000110000110101001101111110010000111110010100110111110000101100101101100011101001111101011011110100101101111101010011110111000100010011100101010111000011010100111110101111001110101001001000111011111001011001110011000000101000010111000000110110010001111101010011111111010010101011100101100101000111010100100101011111010101100111010011111010101011110100000011010100000000001111010111110010101011100101011101000111111101111001000011101101100001011010110010010101011100101110011001100110111101100001010000000110101010101010000001010010110001100100110001000101110111110001100100101001110101110001001010010101011001110011001010011011010011111010010101101000111101100010000001010011000111010011001011111000101101000011011010110100111000100001111100111100100111111110000000110001110110000101010101010111110010101011100011110011110101000011111010011011011101110011111010100111111110101111100101100011001011101011111001111101010111001110010101011111111010000101011111000000011101010101100100101010111101001011001110001010011010000110100000111001111010100000111110111010010101011100101100001011010101010110001111111010001010000001010001000100000011100001101101100101001011010110100111000000011101010110100000011111010011111010101110010100001101011001001101110111010001111011010100010011110010001110110111001001011011010110010010111111010011100001011110010010101011100011110011110010010001010110101101010100111100111111111110110100010010110111101001011011111010100110111011010011001111001010000011110100110001110000001111010111101010011011010101011100101001111111100001111100110000010110000110100001101011110100000011011100010010110010000001010000001101110001001011001000101011010110100110011100101101100001101011010011111011100101010111011001010001110101001001010010110101101001110011000111101110000100011010101110010100010001110011111101000110011111010110111011000001111010001100100101001101000010101001010101110001111000101100100111101110001000100111100100111111101000001001010001011011011101000001110010100110001110010110101101010100011101110001001010010101011110011010111101010000111011111000000011011001110010000001111001101011111010110010010110101101001110001111001011100110011111100101100101111100010000000100001011001001010101010110010111110011111111000000111010011000111101110001110001010100111100101100100111111101000101100101001100100101101011010011100010101100001010100011111100100001101010110000001011001010001010101111010001100111001111111100010110010110111101011011101100011001001010000000010111111010011011000010100110010100000110010110001100101010101100101000001010101010101001010101110011001101010001111001011001010000101010011110110100100011100110110100100100001101010111101100001010111110000001010000001100101100111100101001100110101100110001111011011101000011010111101100100111111110001000100111010111100010011110010111110001100110111101101010000111110011100101110010001101011010110011110001001010101010101111100110011010101110101101100101001111111100000011101000000111111010011001011110011100111110101100111101010000110011111010111110000110100001110110001101100100011010111101100011101010111100101010111000100011001110110110100011000110010110010100001011011001000001010010101011100101010111001101100100011101101110100011111010011011010010010111111010011101100111010111110010100000110100000001010011110010101110001101110001100011001100110101100100000000111010110100101010101100100000010100101100001011101011001110001011111101001110000101111001101111011011111011110000001110100000011001011011000100101010111000000010110111000110011111110100011111011001000000101000001011001011011101101001110110010000110101001011001010001110101001001010001100010010111011001111111011001000110101111011000111000110001100001101010010110010100011101010010010100111100010011101100010101110010100010100001101010001000111111011010001001010111110000001100101111110100011000110101111010001110110101101010100001110100101110001010100111011001001010101110001011111001011011100110111001011110010100011000110001100111000101010000100111011011101100000010100111111110000001110100101100001011101010110100110110110100111010010101011100000011101101001111011011110110000000010001101010111001000100111100101111100011000110011010000101010010110011010000111110010100101010111001111101000111010011011000010100110001110000000010000111110011000110110110010101111100111111101001000111001010000000010000111110010101010101011111001101000010101001011101110001101010011011010010010000110101011100101010111011100010111000011111101110010101111000100101010111101011111000000101000110001111111010000000010100111011110001001010000000110110011100100101100011101101011010011000100001001010111110000001010011001110101110001001110010110111101100111100101001101000010101001111100101101011011000100101010111000000110101000110010001011101001011010110100111000101111101010111001010111001001100011001011000100010010001000100100000101110110011011110'

"""

#%%
'''
Si no tenemos en cuenta la memoria necesaria para almacenar el diccionario, 
¿cuál es la ratio de compresión?
'''

#numero de bits del mensaje codificado / numero de bits del mensaje
c = (len(m)*100)/(len(mensaje.encode('utf-8'))*8)
print("El ratio de compresion es del ", round(c, 2), "%")

'''
Si tenemos en cuenta la memoria necesaria para almacenar el diccionario, 
haz una estimación de la ratio de compresión.
'''

#numero de bits del mensaje codificado + numero de bits del diccionario / numero de bits del mensaje
c = (len(m)*100 + (sys.getsizeof(m2c)*8))/(len(mensaje.encode('utf-8'))*8)
print("El ratio de compresion teniendo en cuenta el diccionario es del ", round(c, 2), "%")


