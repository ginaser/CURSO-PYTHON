
# camelCase

class Mascota(object):

    def __init__(self, nombre, color='negro',edad=1):
        self.nombre = nombre
        self.color= color
        self.edad= edad

    def obtener_nombre(self):
        print 'Dentro de clase base'
        return '{nombre} {color} {edad}'.format(
            nombre=self.nombre,
            color=self.color,
            edad=self.edad
        )

class Gato(object):
      
    def obtener_edad(self):

        return self.edad


class Perro(Mascota, Gato):
    a = 'un attrb'

    def __init__(self, edad, nombre):
        super(Perro, self).__init__(nombre)
        self.edad = edad

if __name__ == '__main__':
    
  
    perro  = Perro(2, 'Fido')

    nombreperro = perro.obtener_nombre()
    print nombreperro
    edadperro = perro.obtener_edad()
    print edadperro

