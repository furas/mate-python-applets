#!/usr/bin/env python3

#
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html
#
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator

APPINDICATOR_ID = 'myappindicator'
ICON = 'whatever'
#ICON = gtk.STOCK_INFO

def main():
    #indicator = appindicator.Indicator.new(APPINDICATOR_ID, ICON, appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, ICON, appindicator.IndicatorCategory.OTHER)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    #indicator.set_menu(gtk.Menu())
    indicator.set_label("Hello World!", APPINDICATOR_ID)
    indicator.set_menu(build_menu())
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    
    item = gtk.MenuItem(label='Quit')
    item.connect('activate', gtk.main_quit)
    menu.append(item)
    
    menu.show_all()
    
    return menu
    
    
if __name__ == '__main__':
    main()
