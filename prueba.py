from gi.repository import Gtk

if __name__ == '__main__':

	ventana = Gtk.Window(title='Ejemplo3')
	ventana.connect('delete-event' , Gtk.main_quit)
	boton = Gtk.Button('Btn 1')
	

	contenedor = Gtk.Grid()
	contenedor.set_column_homogeneous(True)
	contenedor.set_row_homogeneous(False)

	contenedor.attach(
	boton , # Elemento
	1, #columna
	3, #fila
	2, #Nro columnas a usar
	2, #Nro Filas a usar
)
	contenedor.attach(boton, 1, 2, 1, 0)
	ventana.add(contenedor)
	ventana.show_all()
	Gtk.main()