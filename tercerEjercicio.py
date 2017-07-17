import random

MensajeTodosDatos = "El estudiante {0} de {1} es de la ciudad de {2} y cursa {3} en la universidad"
estudainteManagua = "El estudiante {0} de {1} es de la ciudad de {2} y cursa {3} en la universidad"
estudainteMasaya = "El estudiante {0} de {1} es de la ciudad de {2} y cursa {3} en la universidad"
estudainteMenor = "El estudiante {0} de {1} es de la ciudad de {2} y cursa {3} en la universidad"


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

    Diccionario = generar_diccionario_estudiantes()


    
    for datos,values in Diccionario.iteritems():

        print MensajeTodosDatos.format(datos,values['edad'],values['cuidad'],values['anio'])
    
    
    print''
    print 'ESTUDAINTES DE MANAGUA'   
    for datos,values in Diccionario.iteritems():

        if values['cuidad'] == 'Managua':
            
            print estudainteManagua.format(datos,values['edad'],values['cuidad'],values['anio'])
            f = open('ESTUDIANTE_DE_MANAGUA.txt','a')
            f.write(estudainteManagua.format(datos,values['edad'],values['cuidad'],values['anio']))
            f.close()


    print''        
    print 'ESTUDAINTES DE MASAYA QUE CURSAN PRIMER ANIO'   
    for datos,values in Diccionario.iteritems():

        if values['cuidad'] == 'Masaya' and values['anio'] == 1:
            
            print estudainteManagua.format(datos,values['edad'],values['cuidad'],values['anio'])
            f = open('ESTUDIANTE_DE_MASAYA.txt','a')
            f.write(estudainteManagua.format(datos,values['edad'],values['cuidad'],values['anio']))
            f.close()


    print''
    print 'ESTUDAINTES MENOR DE 21'   
    for datos,values in Diccionario.iteritems():

        if values['edad'] < 21 :
            
            print estudainteManagua.format(datos,values['edad'],values['cuidad'],values['anio'])
            f = open('ESTUDIANTE_MENOR.txt','a')
            f.write(estudainteManagua.format(datos,values['edad'],values['cuidad'],values['anio']))
            f.close()

