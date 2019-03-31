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

     
def append_menu(applet):

    menu_xml="""
        <menuitem item="Item 1" action="AboutAction"/>
        <menuitem item="Item 2" action="QuitAction"/>
    """
			
    actions = [
        ('AboutAction', None, 'About Test Applet', None, None, show_dialog),    
        ('QuitAction', None, 'Quit Test Applet', None, None, Gtk.main_quit),    
    ]
    
    action_group = Gtk.ActionGroup("TestApplet") 
    action_group.add_actions(actions, applet)
    applet.setup_menu(menu_xml, action_group)


def applet_fill(applet):

    label = Gtk.Label(label="Label")
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

