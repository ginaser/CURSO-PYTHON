import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def _init_(self, *args, **kwargs):
		super(MiVentana, self)._init_(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)

	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()

	def agregarboton(MiVentana):
		boton2 = Gtk.Button('Boton 2')
		ventana = Gtk.Window(title='Ejemplo3')

		boton.connect = ('Clicked' , imprimir_algo)
		boton2 = Gtk.Button('Boton 2')
	
		contenedor = Gtk.VBox()
	
	

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()
