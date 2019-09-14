#!/usr/bin/env python

# https://www.systutorials.com/docs/linux/man/1-mate-panel-test-applets/

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

# https://github.com/city41/mate-i3-applet/blob/master/log.py

#-------------------------------------------------------------------------------

import os
import sys
import logging
import datetime

#-------------------------------------------------------------------------------

def exception_handler(type, value, traceback):
    logging.exception("Uncaught exception occurred: {}".format(value))

logger = logging.getLogger("MinimalAppletLog")

#logger.setLevel(logging.WARNING)
logger.setLevel(logging.DEBUG)

sys.excepthook = exception_handler

#file_handler = logging.FileHandler(os.path.expanduser("~/.minimalapplet.log"))
file_handler = logging.FileHandler(os.path.expanduser("/home/furas/projekty/python/__MATE__/minimal-applet/applet.log"))
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
from gi.repository import GLib  # timeout_add
                                    
def applet_fill(applet):
    global label
    
    #logger.debug(str(applet))

    # you can use this path with gio/gsettings
    #settings_path = applet.get_preferences_path()
    #logger.debug(settings_path)
    
    box = Gtk.Box()
    applet.add(box)

    label = Gtk.Label()
    box.add(label)
        
    applet.show_all()

    # show first time    
    update_label()
    
    # show again after 1000ms 
    GLib.timeout_add(1000, update_label)
    # Gtk.timeout_add(1000, update_label) # doesn't work in new Gtk

def update_label():
    text = datetime.datetime.now().strftime('[ %Y.%m.%d | %H:%M:%S ]')
    label.set_text(text)
    return True
    
def applet_factory(applet, iid, data):
    if iid != "MinimalApplet":
       return False
 
    applet_fill(applet)
 
    return True

MatePanelApplet.Applet.factory_main("MinimalAppletFactory", True,
                            MatePanelApplet.Applet.__gtype__,
                            applet_factory, None)

