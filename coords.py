#! /usr/bin/env python

# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class Region:

    def __init__(self):
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.track_started = False
        self.track_ended = False


class Coords:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(300,200)

        self.window.add_events(gtk.gdk.MOTION_NOTIFY | gtk.gdk.BUTTON_PRESS)
        self.window.connect("motion_notify_event", self.mouse_moved)
        self.window.connect("destroy", self.destroy)

        self.setup_widgets()

        self.window.show()

        self.root_window = None

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

        self.start_button = start_button
        self.start_button.connect("clicked", self.start)

    def start(self, widget, data=None):
        region = Region()
        mask = gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.BUTTON_RELEASE_MASK
        self.root_window = gtk.gdk.get_default_root_window()
        result = gtk.gdk.pointer_grab(self.root_window, False, mask, None, None)
        self.root_window.add_filter(self.region, region)

    def region(self, event, region):
        x, y, flags = event.window.get_pointer()
        if 'GDK_BUTTON1_MASK' in flags.value_names \
                and region.track_started == False:
            region.start_x = x
            region.start_y = y
            region.track_started = True
            region.track_ended = False
            print 'started'
        if 'GDK_BUTTON1_MASK' not in flags.value_names \
                and region.track_started == True:
            region.end_x = x
            region.end_y = y
            region.track_ended = True
            region.track_started = False
            print 'ended'
            print region.start_x
            print region.start_y
            print region.end_x
            print region.end_y
        return gtk.gdk.FILTER_CONTINUE

    def mouse_moved(self, widget, data=None):
        #print gtk.gdk.display_get_default().get_pointer()
        pass

    def destroy(self, widget, data=None):
        gtk.main_quit()


if __name__ == "__main__":
    coords = Coords()
    coords.main()
