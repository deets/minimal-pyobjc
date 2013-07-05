import sys
from setuptools import setup, find_packages
import glob, subprocess
import os


PROJECT = "Minimal"
ICON = "Minimal.icns"

plist = {
    "CFBundleIconFile" : ICON,
    "CFBundleIdentifier" : "com.minimal-project.%s" % PROJECT,
    }


setup(
    name = "Minimal",
    version = "0.1",
    packages = find_packages(),
    author = "Diez B. Roggisch",
    author_email = "deets@web.de",
    description = "A simple pyobjc project to get you started",
    license = "MIT",
    keywords = "python pyobjc",
    app=["Application.py"],
    data_files=["English.lproj"] +glob.glob("Resources/*.*"),
    options=dict(py2app=dict(
        plist=plist,
    )),
)
