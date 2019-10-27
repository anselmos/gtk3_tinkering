#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2019 [Anselmos](github.com/anselmos) <anselmos@users.noreply.github.com>
#
# Distributed under terms of the MIT license.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from time import sleep

class ContextButton(Gtk.Button):
    def __init__(self, name, ctx):
        super().__init__(name)
        self.ctx = ctx

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label1 = Gtk.Label(data.get('name'), xalign=0)
        label2 = ContextButton(f"ProjectId: {data.get('project_id')}", data)
        vbox.pack_start(label1, True, True, 0)
        vbox.pack_start(label2, True, True, 0)

        switch = Gtk.Switch()
        switch.props.valign = Gtk.Align.CENTER
        hbox.pack_start(switch, False, True, 0)
        self.add(hbox)
        label2.connect("clicked", self.on_box_clicked)
    def on_box_clicked(box, data):
        print(f"on box clicked name: ${data.ctx.get('name')}")

class SimpleList(Gtk.Window):
    task_list  = [ {'id': '111', 'name': 'Apples', 'project_id' : '11'}, {'id': '222', 'name': 'oranges', 'project_id': '22'}]
    def __init__(self):
        Gtk.Window.__init__(self, title="Task List")
        listbox = Gtk.ListBox()

        row = Gtk.ListBoxRow()
        for task in self.task_list:
            row = ListBoxRowWithData(task)
            listbox.add(row)
        self.add(listbox)


        def on_row_activated(listbox, row):
            # this will block UI!
            print('on row activasted')

        listbox.connect('row-activated', on_row_activated)

win = SimpleList()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
