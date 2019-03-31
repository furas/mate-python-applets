#!/usr/bin/env python

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('MatePanelApplet', '4.0')
from gi.repository import Gtk
from gi.repository import MatePanelApplet

                                    
def applet_fill(applet):
 
    # you can use this path with gio/gsettings
    settings_path = applet.get_preferences_path()

    box = Gtk.Box()
    applet.add(box)
    
    label = Gtk.Label(label="TestApplet")
    box.add(label)

    button = Gtk.Button(label="QUIT")
    button.connect('clicked', Gtk.main_quit)
    box.add(button)

    applet.show_all()
     
def applet_factory(applet, iid, data):
    if iid != "TestApplet":
       return False
 
    applet_fill(applet)
 
    return True
 
MatePanelApplet.Applet.factory_main("TestAppletFactory", True,
                                    MatePanelApplet.Applet.__gtype__,
                                    applet_factory, None)

