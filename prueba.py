import argparse

variable_text ='esto es una prueba {0}'

if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	parser.add_argument ('nombre')
	args = parser.parse_args()

	print (args.nombre)
	print (variable_text.format(args.nombre))


	print (variable_text.count('e'))
	print (variable_text.replace ("o","0").format(args.nombre))
	print (len(variable_text))
	print (variable_text.upper())
	