# -*- coding: utf-8 -*-


"""
Dado un mensaje, el tamaño de la ventana de trabajo W, y el tamaño
del buffer de búsqueda S dar la codificación del mensaje usando el
algoritmo LZ77


mensaje='cabracadabrarrarr'
LZ77Code(mensaje,12,18)=[[0, 0, 'c'], [0, 0, 'a'], 
  [0, 0, 'b'], [0, 0, 'r'], [3, 1, 'c'], [2, 1, 'd'], 
  [7, 4, 'r'], [3, 4, 'EOF']]
  
"""
#indexOf nos devuelve la ocurrencia más a la derecha de item en mylist	
#la use en la otra implementación, para esta no la uso en nada	
def indexOf(mylist,item):
	if item in mylist:
		newlist= mylist
		copy=newlist
		while item in newlist:
			copy=newlist
			newlist = newlist[1:]
		relativeindex = copy.index(item)
		return copy.index(item)+len(mylist)-len(copy)
	return -1

def LZ77Code(mensaje,S=12,W=18):
	code=[[0,0,mensaje[0]]]
	mydict=[[0,0,mensaje[0]]]
	i=1#donde estamos leyendo carácteres
	ahead=W-S
	lookahead=mensaje[1:1+ahead]
	old=str(mensaje[max(0,i-S-1):max(0,i)])
	while i < len(mensaje):
		offset=0
		length=0
		char=lookahead[0]
		window = old+lookahead
		#miramos matches 
		for j in range(len(old)-1,-1,-1):
			if old[j] == lookahead[0]:
				#tenemos algun match
				match=True
				izq=j+1
				der=len(old)+1
				maxlen=1
				#longest prefix match
				while match and der <len(window):
					if window[izq] == window[der]:
						izq+=1
						der+=1
						maxlen+=1
					else: 
						match=False
				#extendemos carácteres extra
				if maxlen> length :
					offset= len(old) -j
					length= maxlen
					try :
						char= window[der]
					except:
						try:
							char= window[i+length]
						except:
							char=window[der-1]
							length -=1
							if length == 0:
								offset=0
							
		code=code+[[offset,length,char]]
		i += length+1
		old=str(mensaje[max(0,i-S):i])
		lookahead= str(mensaje[i:ahead+i])
	code[-1]=[code[-1][0],code[-1][1]+1,'EOF']
	return code
      
#print('-----------')
#print('-----------')


mensaje='patatapatapa'
#print(LZ77Code(mensaje,12,18))
#assert(False)
#[[0, 0, 'c'], [0, 0, 'a'],   [0, 0, 'b'], [0, 0, 'r'], [3, 1, 'c'], [2, 1, 'd'],  [7, 4, 'r'], [3, 4, 'EOF']]

"""
Dado un mensaje codificado con el algoritmo LZ77 hallar el mensaje 
correspondiente 

code=[[0, 0, 'p'], [0, 0, 'a'], [0, 0, 't'], [2, 1, 'd'], 
      [0, 0, 'e'], [0, 0, 'c'], [4, 1, 'b'], [0, 0, 'r'], [3, 1, 'EOF']]

LZ77Decode(mensaje)='patadecabra'
"""   
def LZ77Decode(codigo):
	mensaje=''
	for i in codigo:
		if i[0] != 0:
			pos=len(mensaje)-i[0]
			word=mensaje[pos:pos+ i[1]] 
			extension= ""
			mensaje += word 
			if i[0] <= i[1]:#debemos extender el último simbolo
				mensaje += mensaje[i[0]+1:i[1]+1] 
		mensaje+= i[2]
	return mensaje[:-3]
    

code=[[0, 0, 'p'], [0, 0, 'a'], [0, 0, 't'], [2, 1, 'd'], 
      [0, 0, 'e'], [0, 0, 'c'], [4, 1, 'b'], [0, 0, 'r'], [3, 1, 'EOF']]
code=[[0,0 ,'p'],[0,0,'a'], [0,0,'t'],[2,3,'p'],[4,5,'EOF']]
#print(LZ77Decode(code))
#assert(False)
ans= LZ77Code(mensaje,12,18)
#print('***********************')
#print('ans: ' +str(ans))
#print(LZ77Decode(ans))
#assert(False)
    


"""
Jugar con los valores de S y W (bits_o y bits_l)
para ver sus efectos (tiempo, tamaño...)
"""


mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos. La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'

#funcion util para debuggar errores
def difAt(string1,string2):
	i=0
	if len(string1) > len(string2):
		print('String1 is longer') 
		return 'error'
	if len(string1) < len(string2):
		print('String2 is longer') 
		return 'error'
	while i< len(string1):
		if string1[i] != string2[i]:
			print(str(i) + 'th position is different!')
			return 'error'
		i+=1
	return 'ok'		

bits_o=12
bits_l=4
S=2**bits_o
W=2**bits_o+2**bits_l
#print('**************')
mensaje_recuperado2=LZ77Decode(LZ77Code(mensaje,S,W))
#print(LZ77Code(mensaje,S,W))
#print('mensajerecuperado2:'  + mensaje_recuperado2)
#print('mensaje:'  + mensaje)
print('**************')
print('Soniguales?' + str(mensaje==mensaje_recuperado2))
print(difAt(mensaje, mensaje_recuperado2))

import time
start_time = time.clock()
mensaje_codificado=LZ77Code(mensaje,S,W)
print (time.clock() - start_time, "seconds code")
start_time = time.clock()
mensaje_recuperado=LZ77Decode(mensaje_codificado)
print (time.clock() - start_time, "seconds decode")
ratio_compresion=8*len(mensaje)/((bits_o+bits_l+8)*len(mensaje_codificado))
print('Longitud de mensaje codificado:', len(mensaje_codificado))
print('Ratio de compresión:', ratio_compresion)



