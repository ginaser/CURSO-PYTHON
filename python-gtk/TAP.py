

	def agregar_lista(self):
		"""crear un TreeView
		1- crear el modelo de datos (GtK.ListStore(type,type,...,type)
		2- crear el widget que contiene o muestra los datos de modelo.
		TreeView(<model>)
		3- Definir las columnas y su contenido.

		3.1- Crear celda para cada columna de la fila
		Los CellRenderer son widgets que sirven para mostrar contenido dentro de otros widgets dependiendo de su tipo.
		3.2-crear columnas (TreeViewColumn) del TreeView que mostraran los datos usando CellRenderer widgets como elementos hijos
		args(TItulo, cellRenderer, posicion en el modelo de la info a mostrar.)
		3.3 Agregar cada TreeViewColumn al TreeView widget
		"""
		self.modelo = Gtk.ListStore(str, float)
		self.modelo.append(['Valor 1', 1.5])

		self.lista_activos = Gtk.TreeView(self.modelo)

		descripcion = Gtk.CellRendererText()
		columna_descripcion = Gtk.TreeViewColumn(
			'Descripcion', 
			descripcion, 
			text=0
		)

		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto' , monto, text=1)

		self.lista_activos.append_column(columna_descripcion)
		self.lista_activos.append_column(columna_monto)

		self.lista_pasivos= Gtk.TreeView(self.modelo)

		descripcion = Gtk.CellRendererText()
		columna_descripcion = Gtk.TreeViewColumn(
			'Descripcion', 
			descripcion, 
			text=0
		)

		monto = Gtk.CellRendererText()
		columna_monto = Gtk.TreeViewColumn('Monto' , monto, text=1)

		self.lista_pasivos.append_column(columna_descripcion)
		self.lista_pasivos.append_column(columna_monto)


		self.contenedor.attach_next_to(
			self.lista_activos,
			self.boton,
			Gtk.PositionType.BOTTOM,
			1,
			1
		)

		self.boton.connect('clicked', self.agregar_fila)


		self.contenedor.attach_next_to(
			self.lista_pasivos,
			self.boton,
			Gtk.PositionType.RIGHT,
			1,
			1
		)

		self.boton.connect('clicked', self.agregar_fila)

	def agregar_fila(self, btn):
		texto = self.entrada.get_text()
		monto =  self.entrada_monto.get_text()
		self.modelo.append([texto, float,(monto)])