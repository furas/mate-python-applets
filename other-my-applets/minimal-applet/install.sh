#!/bin/bash

NAME=MinimalApplet

# SRC = SOURCE, DST = DESTINATION

SRC_FOLDER=.

SRC_NAME1=${NAME}.mate-panel-applet
DST_NAME1=${NAME}.mate-panel-applet
#DST_NAME1=org.mate.panel.${NAME}.mate-panel-applet

SRC_NAME2=${NAME}Factory.service
DST_NAME2=${NAME}Factory.service
#DST_NAME2=org.mate.panel.applet.${NAME}Factory.service

cp ${SRC_FOLDER}/${SRC_NAME1} /usr/share/mate-panel/applets/${DST_NAME1}
cp ${SRC_FOLDER}/${SRC_NAME2} /usr/share/dbus-1/services/${DST_NAME2}

