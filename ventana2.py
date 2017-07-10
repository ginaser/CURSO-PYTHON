import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def imprimir_algo(btn):
	print btn
	print 'HOLA MUNDO'

if __name__ == '__main__':

	ventana = Gtk.Window(title='Ejemplo2')
	ventana.connect('delete-event' , Gtk.main_quit)
	boton = Gtk.Button('Btn 1')
	#boton.connect('clicked',imprimir_algo)
	boton2 = Gtk.Button('Boton 2')

	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)

	contenedor.attach(
	boton , # Elemento
	0, #columna
	0, #fila
	1, #Nro columnas a usar
	1, #Nro Filas a usar
)
	contenedor.attach(boton2, 0, 1, 1, 1)
	ventana.add(contenedor)
	ventana.show_all()
	Gtk.main()