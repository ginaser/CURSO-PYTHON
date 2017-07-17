import random

NOMBRES = [
    'Ana',
    'Pedro',
    'Pablo',
    'Ernesto',
    'Ariel',
    'Carlos',
    'Luis',
    'Oscar',
    'Alicia',
    'Maria',
    'Brenda'
]

CIUDADES = [
    'Managua',
    'Masaya',
    'Matagalpa',
    'Chinandega',
    'Somoto',
    'Rivas'
]

MensajeTodosDatos = "El estudiante {nombre_estudiante} de <edad> es de la ciudad de {ciudad} y cursa {anio} en la universidad"

def generar_diccionario_estudiantes():
    estudiantes = {}

    for nombre in NOMBRES:
        estudiantes[nombre] = {
            'edad': random.randrange(16, 30),
            'anio': random.randrange(1, 5),
            'cuidad': random.choice(CIUDADES)
        }

	return estudiantes


if __name__ == '__main__':
	dic = generar_diccionario_estudiantes()


	for datos in dic.iteritems():
		print(datos)	
		



		