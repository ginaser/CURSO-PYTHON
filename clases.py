
# camelCase

class Mascota(object):

    def __init__(self, nombre, color='negro'):
        self.nombre = nombre
        self.color= color

    def obtener_nombre(self):
        print 'Dentro de clase base'
        return '{nombre} {color}'.format(
            nombre=self.nombre,
            color=self.color
        )

class Gato(object):
      
    def obtener_nombre(self):

        return self.nombre

    def obtener_edad(self):

        return self.edad


class Perro(Mascota, Gato):
    a = 'un attrb'

    def __init__(self, edad, nombre):
        super(Perro, self).__init__(nombre)
        self.edad = edad


    def obtener_nombre(self):
        print 'metodo de subclase'
        nombre = super(Perro, self).obtener_nombre()
        print nombre
        return nombre


    def obtener_edad(self):
        print 'metodo de subclase'
        edad = super(Perro, self).obtener_edad()
        print edad
        return edad
 


if __name__ == '__main__':
    
  
    perro  = Perro('mascota', 'nombre mascota')

    nombreperro = perro.obtener_nombre()
    print nombreperro

    print perro.obtener_edad()
