#! /usr/bin/env python

# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk


class Coords:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(300,200)

        self.window.connect("destroy", self.destroy)

        self.setup_widgets()

        self.window.show()

    def main(self):
        gtk.main()

    def setup_widgets(self):
        start_label = gtk.Label("start")
        start_x_label = gtk.Label("x")
        start_y_label = gtk.Label("y")
        start_x = gtk.Label("this will be x")
        start_y = gtk.Label("this will be y")

        end_label = gtk.Label("end")
        end_x_label = gtk.Label("x")
        end_y_label = gtk.Label("y")
        end_x = gtk.Label("this will be x")
        end_y = gtk.Label("this will be y")

        width_label = gtk.Label("width")
        width = gtk.Label("this will be w")

        height_label = gtk.Label("height")
        height = gtk.Label("this will be h")

        start_button = gtk.Button("start")
        reset_button = gtk.Button("reset")

        hbox_one = gtk.HBox(gtk.TRUE, 10)
        hbox_one.pack_start(start_label)
        hbox_one.pack_start(start_x_label)
        hbox_one.pack_start(start_x)

        hbox_two = gtk.HBox(gtk.TRUE, 10)
        hbox_two.pack_start(start_y_label)
        hbox_two.pack_start(start_y)

        hbox_three = gtk.HBox(gtk.TRUE, 10)
        hbox_three.pack_start(end_label)
        hbox_three.pack_start(end_x_label)
        hbox_three.pack_start(end_x)

        hbox_four = gtk.HBox(gtk.TRUE, 10)
        hbox_four.pack_start(end_y_label)
        hbox_four.pack_start(end_y)

        hbox_five = gtk.HBox(gtk.TRUE, 10)
        hbox_five.pack_start(width_label)
        hbox_five.pack_start(width)
        hbox_five.pack_start(start_button)

        hbox_six = gtk.HBox(gtk.TRUE, 10)
        hbox_six.pack_start(height_label)
        hbox_six.pack_start(height)
        hbox_six.pack_start(reset_button)

        main_box = gtk.VBox(gtk.TRUE, 10)
        main_box.pack_start(hbox_one)
        main_box.pack_start(hbox_two)
        main_box.pack_start(hbox_three)
        main_box.pack_start(hbox_four)
        main_box.pack_start(hbox_five)
        main_box.pack_start(hbox_six)
        
        start_label.show()
        start_x_label.show()
        start_x.show()
        hbox_one.show()

        start_y_label.show()
        start_y.show()
        hbox_two.show()

        end_label.show()
        end_x_label.show()
        end_x.show()
        hbox_three.show()

        end_y_label.show()
        end_y.show()
        hbox_four.show()

        width_label.show()
        width.show()
        start_button.show()
        hbox_five.show()

        height_label.show()
        height.show()
        reset_button.show()
        hbox_six.show()

        self.window.add(main_box)
        main_box.show()

    def destroy(self, widget, data=None):
        gtk.main_quit()


if __name__ == "__main__":
    coords = Coords()
    coords.main()
