#! /usr/bin/env python

# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk


class Coords:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)

        self.window.connect("destroy", self.destroy)

        self.window.show()

    def main(self):
        gtk.main()

    def destroy(self, widget, data=None):
        gtk.main_quit()


if __name__ == "__main__":
    coords = Coords()
    coords.main()
