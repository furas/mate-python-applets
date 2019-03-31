#!/usr/bin/env python

# now Ctrl+C will break program if you run it in terminal
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
#--------------------------------------------------------

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('MatePanelApplet', '4.0')
from gi.repository import Gtk
from gi.repository import MatePanelApplet

                                    
def applet_fill(applet):

    label = Gtk.Label(label="My Label")
    applet.add(label)
    applet.show_all()

    append_menu(applet)

     
def applet_factory(applet, iid, data):
    if iid != "TestApplet":
       return False
 
    applet_fill(applet)
 
    return True


MatePanelApplet.Applet.factory_main("TestAppletFactory", True,
                            MatePanelApplet.Applet.__gtype__,
                            applet_factory, None)

