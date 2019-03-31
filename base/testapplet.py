#!/usr/bin/env python

# https://www.systutorials.com/docs/linux/man/1-mate-panel-test-applets/

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# https://github.com/city41/mate-i3-applet/blob/master/log.py


import os
import sys
import logging

def exception_handler(type, value, traceback):
    logging.exception("Uncaught exception occurred: {}".format(value))

logger = logging.getLogger("TestAppletLog")

#logger.setLevel(logging.WARNING)
logger.setLevel(logging.DEBUG)

sys.excepthook = exception_handler

file_handler = logging.FileHandler(os.path.expanduser("~/.testapplet.log"))
file_handler.setFormatter(
    logging.Formatter('[%(levelname)s] %(asctime)s: %(message)s', "%Y-%m-%d %H:%M:%S")
)
logger.addHandler(file_handler)

#-------------------------------------------------------------------------------

import gi
gi.require_version("Gtk", "3.0")
gi.require_version('MatePanelApplet', '4.0')
from gi.repository import Gtk
from gi.repository import MatePanelApplet
from gi.repository import Gdk

                                    
def applet_fill(applet):
    logger.debug("applet_fill")
    logger.debug(str(applet))
    
    # you can use this path with gio/gsettings
    settings_path = applet.get_preferences_path()

    box = Gtk.Box()
    applet.add(box)

    label = Gtk.Label(label="Label")
    box.add(label)
        
    button = Gtk.Button(label="Dialog")
    button.connect('clicked', show_dialog)
    #button.connect('clicked', create_menu, applet)
    #button.connect("button-press-event", showMenu, applet)
    #button.connect("clicked", showMenu, applet)
    box.add(button)

    button = Gtk.Button(label="Quit")
    button.connect('clicked', Gtk.main_quit)
    box.add(button)

    #applet.add_menu(build_menu())
    applet.show_all()

    append_menu(applet)

    
#def create_menu(widget, event, applet):
#    f = open('log', 'w')
#    f.write(str(widget)+'\n')
#    f.write(str(event)+'\n')
#    f.write(str(applet)+'\n')
#    f.close()

#    menu_xml='<popup name="button3"><menuitem verb="About" label="AKUKU"/></popup>'    
#    menu_xml='''<popup name="button3">
#			<menuitem name="Item 3" verb="About" label="_About" pixtype="stock" pixname="Gtk-about"/>
#			</popup>'''    
#    verbs = [("About", showAboutDialog)]
#    applet.setup_menu(menu_xml, verbs, None)


def show_menu(widget, event, applet):
    # https://developer.gnome.org/gdk3/stable/gdk3-Event-Structures.html#GdkEventButton

    logging.debug("show_menu")
    
    #if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 1:
    if event.button == 1:
        logging.debug("show_menu - button 1")
        #showMainDialog()
        #show_dialog(widget)
        create_menu(applet)
    #if event.type == Gdk.EventType.BUTTON_PRESS and event.button == 3:
#    elif event.button == 3:
#        logging.debug("show_menu - button 3")
#        widget.emit_stop_by_name("button-press-event")
#        create_menu(applet)


def append_menu(applet):
    logging.debug("append_menu")

    #propxml="""<popup name="button3">
    #           <menuitem name="Item 3" action="AboutAction" label="_About"/>
    #			</popup>"""

			    
    # https://github.com/mate-desktop/mate-applets/blob/master/mateweather/mateweather-applet.c
    # https://github.com/mate-desktop/mate-applets/blob/master/mateweather/mateweather-applet-menu.xml

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


def show_dialog(widget, event=None):
    logging.debug("show_dialog")
    logging.debug(str(widget))
    logging.debug(str(event))

    win = Gtk.Window()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()

     
def applet_factory(applet, iid, data):
    if iid != "TestApplet":
       return False
 
    applet_fill(applet)
 
    return True

MatePanelApplet.Applet.factory_main("TestAppletFactory", True,
                            MatePanelApplet.Applet.__gtype__,
                            applet_factory, None)

