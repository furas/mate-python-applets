#!/usr/bin/env python

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('MatePanelApplet', '4.0')
from gi.repository import Gtk
from gi.repository import MatePanelApplet

                                    
def show_dialog(widget, event=None):
    win = Gtk.Window()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()

     
def applet_fill(applet):

    button = Gtk.Button(label="My Button")
    button.connect('clicked', show_dialog)
    applet.add(button)

    applet.show_all()

    
def applet_factory(applet, iid, data):
    if iid != "TestApplet":
       return False
 
    applet_fill(applet)
 
    return True


MatePanelApplet.Applet.factory_main("TestAppletFactory", True,
                            MatePanelApplet.Applet.__gtype__,
                            applet_factory, None)

