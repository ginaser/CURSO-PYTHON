import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import sys



class MyWindow(Gtk.ApplicationWindow):
    

    def __init__(self, app):
        Gtk.Window.__init__(self, title="BIENVENID@", application=app)
        self.set_default_size(300, 200)

        label = Gtk.Label()
        
        label.set_text("SISTEMA SOLAR")

        self.add(label)

class MyApplication(Gtk.Application):

    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = MyWindow(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='SISTEMA SOLAR')
        self.overlay = Gtk.Overlay()
        self.add(self.overlay)
        self.background = Gtk.Image.new_from_file('images/ssolar.gif')
        self.overlay.add(self.background)
        self.grid = Gtk.Grid()
        self.button1 = Gtk.Button(label='SISTEMA SOLAR')
        self.button2 = Gtk.Button(label='PLANETAS')
        self.button3 = Gtk.Button(label='TEST')
        self.grid.add(self.button1)
        self.grid.add(self.button2)
        self.grid.add(self.button3)
        self.overlay.add_overlay(self.grid)


window = MyWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()

