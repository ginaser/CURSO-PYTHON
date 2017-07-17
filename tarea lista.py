
lista = []
SegundaLista = []

if __name__ == '__main__':
		
	def llenarlista():
		for x in range(4):
			num=input("Introducir un numero #--->")
			lista.insert(0,num)
	
	def nuevaLista():
		LongLista = (len(lista))
		for x in range(2):
			if x == 0 :
				SegundaLista.insert(0,lista[LongLista-LongLista])
			else:
				SegundaLista.insert(0,lista[LongLista-1])
	
	def imprimir():
		longLista=(len(lista))
		print()
		print('primer Elemento de la lista-->'+lista[longLista-longLista])
		print("Ultimo Elemento de la lista-->"+lista[longLista-1]+'\n')
		for x in range(len(SegundaLista)):
			print("Elementos de la nueva lista"+ SegundaLista[x])
		
	llenarlista()
	nuevaLista()
	imprimir()

