#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import kde4
from pisi.actionsapi import pisitools

def setup():
    kde4.configure()

def build():
    kde4.make()

def install():
    kde4.install()
    
    pisitools.dodoc("AUTHORS", "LICENSE", "ChangeLog", "TODO", "INSTALL", "README")
    
    pisitools.insinto("/usr/share/pixmaps/", "streams/icons/stream.png", "cantata.png")