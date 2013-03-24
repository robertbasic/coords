#! /usr/bin/env python

# -*- coding: utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class Region:

    def __init__(self):
        self.reset()

    def get_width(self):
        return max(self.start_x, self.end_x) - min(self.start_x, self.end_x)

    def get_height(self):
        return max(self.start_y, self.end_y) - min(self.start_y, self.end_y)

    def reset(self):
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0
        self.track_started = False
        self.track_ended = False


class Coords:

    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_default_size(300,200)

        self.window.connect("destroy", self.destroy)

        self.setup_widgets()
        self.setup_crosshair_cursor()

        self.window.show_all()

        self.root_window = None

        self.region = Region()

    def main(self):
        gtk.main()

    def setup_widgets(self):
        start_label = gtk.Label("start")
        start_x_label = gtk.Label("x")
        start_y_label = gtk.Label("y")
        start_x = gtk.Label("0")
        start_y = gtk.Label("0")

        end_label = gtk.Label("end")
        end_x_label = gtk.Label("x")
        end_y_label = gtk.Label("y")
        end_x = gtk.Label("0")
        end_y = gtk.Label("0")

        width_label = gtk.Label("width")
        width = gtk.Label("0")

        height_label = gtk.Label("height")
        height = gtk.Label("0")

        start_button = gtk.Button("track")
        reset_button = gtk.Button("reset")

        table = gtk.Table(6, 3, False)
        table.attach(start_label, 0, 1, 0, 1)
        table.attach(start_x_label, 1, 2, 0, 1)
        table.attach(start_x, 2, 3, 0, 1)
        table.attach(start_y_label, 1, 2, 1, 2)
        table.attach(start_y, 2, 3, 1, 2)

        table.attach(end_label, 0, 1, 2, 3)
        table.attach(end_x_label, 1, 2, 2, 3)
        table.attach(end_x, 2, 3, 2, 3)
        table.attach(end_y_label, 1, 2, 3, 4)
        table.attach(end_y, 2, 3, 3, 4)

        table.attach(width_label, 0, 1, 4, 5)
        table.attach(width, 1, 2, 4, 5)
        table.attach(start_button, 2, 3, 4, 5)
        table.attach(height_label, 0, 1, 5, 6)
        table.attach(height, 1, 2, 5, 6)
        table.attach(reset_button, 2, 3, 5, 6)

        self.window.add(table)

        self.start_button = start_button
        self.start_button.connect("clicked", self.start_tracking)

        reset_button.connect('clicked', self.reset)

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.width = width
        self.height = height

    def setup_crosshair_cursor(self):
        self.crosshair_cursor = gtk.gdk.Cursor(gtk.gdk.CROSSHAIR)

    def reset(self, widget, data=None):
        self.region.reset()
        self.show_region_values(self.region)

    def start_tracking(self, widget, data=None):
        mask = gtk.gdk.POINTER_MOTION_MASK | gtk.gdk.BUTTON_PRESS_MASK | gtk.gdk.BUTTON_RELEASE_MASK
        self.root_window = gtk.gdk.get_default_root_window()
        # grabs the pointer on the root window for the mask events
        # don't forget to ungrab the pointer later on otherwise uh-oh!
        gtk.gdk.pointer_grab(self.root_window, False, mask, None, self.crosshair_cursor)
        # listening to events from x11 before they get to gtk
        # or something like that
        self.root_window.add_filter(self.track_region, self.region)

    def track_region(self, event, region):
        # i think event is always gtk.gdk.NOTHING
        # but somehow it... works. don't know why or how
        x, y, flags = event.window.get_pointer()
        if 'GDK_BUTTON1_MASK' in flags.value_names \
                and region.track_started == False:
            region.start_x = x
            region.start_y = y
            region.track_started = True
            region.track_ended = False
        if 'GDK_BUTTON1_MASK' not in flags.value_names \
                and region.track_started == True:
            region.end_x = x
            region.end_y = y
            region.track_ended = True
            region.track_started = False
            # ungrab the pointer so we get control back
            gtk.gdk.pointer_ungrab()
            self.show_region_values(region)
        # let the event bubble up to gtk
        return gtk.gdk.FILTER_CONTINUE

    def show_region_values(self, region):
        self.start_x.set_text('%s' % region.start_x)
        self.start_y.set_text('%s' % region.start_y)
        self.end_x.set_text('%s' % region.end_x)
        self.end_y.set_text('%s' % region.end_y)
        self.width.set_text('%s' % region.get_width())
        self.height.set_text('%s' % region.get_height())

    def destroy(self, widget, data=None):
        gtk.main_quit()


if __name__ == "__main__":
    coords = Coords()
    coords.main()
