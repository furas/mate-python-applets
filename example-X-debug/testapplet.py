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

                                    
def show_dialog(widget, event=None):
    logging.debug("show_dialog: widget: {}".format(widget))
    logging.debug("show_dialog: event: {}".format(event))

    win = Gtk.Window()
    win.connect('destroy', Gtk.main_quit)
    win.show_all()

    Gtk.main()

     
def append_menu(applet):
    logging.debug("append_menu: applet: {}".format(applet))

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


def on_button_click(widget, event=None, applet=None):
    # https://developer.gnome.org/gdk3/stable/gdk3-Event-Structures.html#GdkEventButton

    logging.debug("on_button_click: widget: {}".format(widget))
    logging.debug("on_button_click: event: {}".format(event))
    logging.debug("on_button_click: applet: {}".format(applet))
    
    # it may not need to check `event.type` if you assign to `button-press-event`
    #if event.type == Gdk.EventType.BUTTON_PRESS:
    if event.button == 1:
        logging.debug("on_button_click: left button")
        show_dialog(widget)
#    elif event.button == 3:
#        logging.debug("on_button_click: right button")
#        widget.emit_stop_by_name("button-press-event") # stop standard menu on right click ???
#        create_menu(applet)


def applet_fill(applet):
    logger.debug("applet_fill: applet: {}".format(applet))
    
    # you can use this path with gio/gsettings
    settings_path = applet.get_preferences_path()

    box = Gtk.Box()
    applet.add(box)

    label = Gtk.Label(label="Test Applet")
    box.add(label)
        
    button = Gtk.Button(label="Dialog")
    #button.connect('clicked', on_button_click)
    button.connect("button-press-event", showMenu, applet) # it can be also with underscores "button_press_event"
    box.add(button)

    button = Gtk.Button(label="Quit")
    button.connect('clicked', Gtk.main_quit)
    box.add(button)

    applet.show_all()

    # extends right click menu 
    append_menu(applet)
    

def applet_factory(applet, iid, data):
    if iid != "TestApplet":
       return False
 
    applet_fill(applet)
 
    return True


MatePanelApplet.Applet.factory_main("TestAppletFactory", True,
                            MatePanelApplet.Applet.__gtype__,
                            applet_factory, None)

