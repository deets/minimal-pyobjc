#!/bin/bash

NAME=Minimal-0.1
PYTHON=/Library/Frameworks/Python.framework/Versions/2.7/bin/python2.7

rm -rf dist build

$PYTHON setup.py py2app 

if [ -e $NAME.dmg ]; then
    rm $NAME.dmg
fi

hdiutil create -volname $NAME -srcdir dist $NAME.dmg
