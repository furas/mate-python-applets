#!/usr/bin/env python

#-------------------------------------------------------------------------------
# DOESN"T WORK YET
#-------------------------------------------------------------------------------

# TODO: 
# uruchamianie z opcją debug: https://saravananthirumuruganathan.wordpress.com/2010/01/15/creating-gnome-panel-applets-in-python/
# obiektowy programowanie:    https://saravananthirumuruganathan.wordpress.com/2010/01/15/creating-gnome-panel-applets-in-python/

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

try:    
    class MinimalApplet(object):
                                        
        def __init__(self, applet):
            
            logger.debug('__init__')

            # you can use this path with gio/gsettings
            #settings_path = applet.get_preferences_path()
            #logger.debug(settings_path)
            
            self.box = Gtk.Box()
            applet.add(self.box)

            self.label = Gtk.Label()
            self.box.add(self.label)
                
            applet.show_all()

            # show first time    
            self.update_label()
            
            # show again after 1000ms 
            GLib.timeout_add(1000, self.update_label)
            # Gtk.timeout_add(1000, update_label) # doesn't work in new Gtk

        def update_label(self):
            text = datetime.datetime.now().strftime('[JEŻ][ %Y.%m.%d | %H:%M:%S ]')
            self.label.set_text(text)
            return True
        
    def applet_factory(applet, iid, data):
        logger.debug(str(iid))

        if iid != "MinimalApplet":
           return False

        try:
            app = MinimalApplet(applet)
        except Exception as ex:
            logger.debug(str(ex))
     
        return True

    MatePanelApplet.Applet.factory_main("MinimalAppletFactory", True,
                                MatePanelApplet.Applet.__gtype__,
                                applet_factory, None)
except Exception as ex:
    logger.debug(str(ex))

