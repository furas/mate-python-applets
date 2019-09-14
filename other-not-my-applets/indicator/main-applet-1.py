#!/usr/bin/env python3

#
# https://ubuntu-mate.community/t/developing-a-panel-applet/3593/8
# https://ubuntu-mate.community/t/python-menu-panel-applet/9376/2
# https://wiki.mate-desktop.org/docs:devel:mate-panel
# 


import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version("Gtk", "3.0")
gi.require_version("MatePanelApplet", "4.0")
from gi.repository import Gtk
from gi.repository import MatePanelApplet

# create the applet

def applet_fill(applet):

    Button = Gtk.ToggleButton("Button on panel")
    applet.add(Button)
    applet.show_all()

# this is called by mate-panel on applet creation

def applet_factory(applet, iid, data):
    if iid != "MateUserMenuApplet":
        return False
    applet_fill(applet)
    return True

MatePanelApplet.Applet.factory_main(
    "MateUserMenuAppletFactory", 
    True,
    MatePanelApplet.Applet.__gtype__,
    applet_factory, 
    None
)
