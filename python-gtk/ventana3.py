import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_boton()
		self.agregar_texto()
		self.agregar_etiqueta()

		
	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
	
	def agregar_texto(self):
		entrada = Gtk.Entry()
		self.contenedor.attach(
			entrada,
			0,
			0,
			3,
			1
		)

	def agregar_boton(self):
		Ventana = Gtk.Window(title = 'MENSAJE')
		boton = Gtk.Button('Boton 1')
		

	def agregar_etiqueta(self):
		etiqueta = Gtk.Label()
		

if __name__ == '__main__':
	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()