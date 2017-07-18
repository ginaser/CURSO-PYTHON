import gi

gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class MiVentana(Gtk.Window):
	def __init__(self,*args,**kwargs):
		super(MiVentana,self).__init__(*args,**kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event',Gtk.main_quit)
		self.agregar_contenedor()
		self.agregar_entrada_activo()
		self.agregar_boton_activo()
		self.agregar_lista_activo()
		self.agregar_boton_pasivo()
		self.agregar_entrada_pasivo()
		
		self.agregar_listaPasivo()



	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)


	def agregar_entrada_activo (self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada,0,0,2,1)
		self.entradaMonto = Gtk.Entry()
		self.contenedor.attach(self.entradaMonto,2,0,1,1)
		


	def agregar_boton_activo(self):
		self.boton = Gtk.Button('Agregar')
		self.label = Gtk.Label()
		self.contenedor.attach_next_to(self.label, self.entrada, Gtk.PositionType.BOTTOM, 3,1)

		self.contenedor.attach_next_to(
			self.boton,
			self.label,
			Gtk.PositionType.BOTTOM,
			3,
			1
			)
		self.label_act = Gtk.Label('Total Activo:')
		self.contenedor.attach(self.label_act,0,9,2,1)
		
		

	def agregar_lista_activo(self):

		self.modelo = Gtk.ListStore(str,float)
		self.lista_activos = Gtk.TreeView(self.modelo)

		descripcion = Gtk.CellRendererText()
		columna_descripcion = Gtk.TreeViewColumn('Descripcion',descripcion,text=0)

		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto',monto,text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)

		self.contenedor.attach_next_to(
			self.lista_activos,
			self.boton,
			Gtk.PositionType.BOTTOM,
			3, 
			1)
		self.boton.connect('clicked',self.agregar_fila_activo)


	def agregar_fila_activo(self,btn):
		self.temp_activo = 0


		if self.entrada.get_text() and self.entradaMonto.get_text():
			textoDescrip = self.entrada.get_text()
			textoMonto = self.entradaMonto.get_text()
			self.modelo.append([textoDescrip,float(textoMonto)])
			self.entrada.set_text('')
			self.entradaMonto.set_text('')
			self.label.set_text("")


			for fila_activo in self.modelo:
				
				total = float(fila_activo[1])
				self.temp_activo += total


			msj = 'Total Activo {0}'

			self.label_act.set_text(msj.format((str(self.temp_activo))))
			self.capital()


		else:
			self.label.set_markup('inserte valores')



	def agregar_entrada_pasivo (self):
		self.entrada_pasivo = Gtk.Entry()
		self.contenedor.attach_next_to(self.entrada_pasivo, self.boton1,Gtk.PositionType.TOP,2,1)
		self.entradaMonto_pasivo = Gtk.Entry()
		self.contenedor.attach_next_to(self.entradaMonto_pasivo, self.entrada_pasivo,Gtk.PositionType.RIGHT,1,1)
	

	def agregar_boton_pasivo(self):
		self.boton1 = Gtk.Button('Agregar')
		self.contenedor.attach(self.boton1,0,6,3,1)
		self.label_pasivo = Gtk.Label()
		self.contenedor.attach(self.label_pasivo,0,4,3,1)
		self.label_pas = Gtk.Label('Total Pasivo')
		self.contenedor.attach(self.label_pas,0,10,2,1)
		self.label_capital = Gtk.Label('Capital:')
		self.contenedor.attach(self.label_capital,0,11,2,1)



	def agregar_listaPasivo(self):

		self.modelo1 = Gtk.ListStore(str,float)
		self.lista_pasivo = Gtk.TreeView(self.modelo1)

		descripcionPasivo = Gtk.CellRendererText()
		columna_descripcionPasivo = Gtk.TreeViewColumn('Descripcion',descripcionPasivo,text=0)

		montoPasivo = Gtk.CellRendererText()
		columna_montoPasivo = Gtk.TreeViewColumn('Monto',montoPasivo,text=1)

		self.lista_pasivo.append_column(columna_descripcionPasivo)
		self.lista_pasivo.append_column(columna_montoPasivo)

		self.contenedor.attach_next_to(
			self.lista_pasivo,
			self.boton1,
			Gtk.PositionType.BOTTOM,
			3, 
			1)

		self.boton1.connect('clicked',self.agregar_fila_pasivo)



	def agregar_fila_pasivo(self,btn):
		self.temp_pasivo = 0

		if self.entrada_pasivo.get_text() and self.entradaMonto_pasivo.get_text():

			textoDescrip_pasivo = self.entrada_pasivo.get_text()
			textoMonto_pasivo = self.entradaMonto_pasivo.get_text()
			self.modelo1.append([textoDescrip_pasivo,float(textoMonto_pasivo)])
			self.entrada_pasivo.set_text('')
			self.entradaMonto_pasivo.set_text('')
			self.label_pasivo.set_text("")

			
			for fila_pasivo in self.modelo1:
				
				total = float(fila_pasivo[1])
				self.temp_pasivo += total


			m = 'Total Pasivo {0}'

			self.label_pas.set_text(m.format((str(self.temp_pasivo))))
			self.capital()
	

		else:
			self.label_pasivo.set_markup(' inserte valores ')


	def capital (self):

		self.temp_capital = 0

		self.temp_capital = float(self.temp_activo) - float(self.temp_pasivo)

		msjcapital = 'Capital {0}'
		self.label_capital.set_text(msjcapital.format(self.temp_capital))

		print temp_capital

	

if __name__ == '__main__':

	ventana = MiVentana()
	ventana.show_all()
	Gtk.main()