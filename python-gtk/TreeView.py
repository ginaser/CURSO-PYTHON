import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MiVentana(Gtk.Window):
	def __init__(self, *args, **kwargs):

		super(MiVentana, self).__init__(*args, **kwargs)
		self.set_default_size(500,300)
		self.connect('delete-event', Gtk.main_quit)

		self.agregar_contenedor()
		self.agregar_entrada()
	
		
	def agregar_contenedor(self):
		self.contenedor = Gtk.Grid()
		self.contenedor.set_column_homogeneous(True)
		self.add(self.contenedor)

	def agregar_entrada(self):
		self.entrada = Gtk.Entry()
		self.contenedor.attach(self.entrada, 0, 0, 1, 1)

	def agregar_boton(self):
		self.boton = Gtk.Button('Agregar')
		self.contenedor.attach_next_to(
			self.boton,
			self.entrada,
			Gtk.PositionType.BOTTOM,
			1,
			1
		)

	def agregar_lista(self):
		"""crear un TreeView
		1- crear el omdel de datos (GtK.ListStore(type,tyoe,...,type)
		2- crear el widget que contiene o muestra los datos de modelo.
		TreeView(<model>)
		3- Definir las columnas y su contenido.

		3.1- Crear celda para cada columna de la fila
		Los CellRenderer son widgets que sirven para mostrar contenido dentro de otros widgets dependiendo de su tipo.
		3.2-crear columnas (TreeViewColumn) del TreeView que mostraran los datos usando CellRenderer widgets como elementos hijos
		args(TItulo, cellRenderer, posicion en el modelo de la info a mostrar.)
		3.3 Agregar cada TreeViewColumn al TreeView widget
		"""
		self.modelo = GtK.ListStore(str, float)
		self.modelo.append(['Valor 1', 1.5])

		self.lista_activos = Gtk.TreeView(self.modelo)

		descripcion = Gtk.CellRendererText()
		columna_descripcion =Gtk.TreeViewColumn(
			'Descripcion', 
			descripcion, 
			text=0
		)

		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto' , monto, text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)


		self.contenedor.attach_next_to(
			self.lista_activos,
			self.boton,
			Gtk.PositionType.BOTTOM,
			1,
			1
		)


