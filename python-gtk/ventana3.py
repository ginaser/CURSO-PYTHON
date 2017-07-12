import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def ___init___(self, *args, **kwargs):
		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)
		
		self.agregar_button()
		self.agregar_txt()
		self.agregar_label()
		self.btnsalir()

		self.box = Gtk.Vbox()
		self.box.pack_start(self.texto, True,True,0)
		self.box.pack_start(self.btn1, True,True,0)
		self.box.pack_start(self.label1, True,True,0)
		self.box.pack_start(self.btnsalir, True,True,0)

		self.add(self.box)

	def imprimir(self,btn):
		imprimir = self.texto.get_text()
		self.label1.set_text(imprimir)


	def agregar_button(self):
		self.btn1 = Gtk.Button('Enviar valor')
		self.btn1.connect('clicked', self.imprimir)

	def agregar_txt(self):
		self.texto = Gtk.Entry()

	def agregarlabel(self):
		self.label1 = Gtk.label('atrapa el valor del textbox')

	def btnsalir(self):
		self.btnsalir = Gtk.Button ('salir')
		self.btnsalir.connect('clicked', Gtk.main_quit)

if __name__ == '__main__':
		ventana = MiVentana()
		ventana.show_all()
		Gtk.main()