# -*- coding: utf-8 -*-

"""Main module."""

from time import sleep
from threading import Thread
from functools import partial
import random

from tornado import gen
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import DataTable, TableColumn, Button

class Drawer:
    """ Object drawer"""

    def __init__(self):
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None,
                             title="Live object positions monitor")

    def create_labeled_circles(self, source_data):
        """ Creates circles representation for a given data source """
        self.figure.circle(x='x', y='y', source=source_data, size=20, color="color", alpha=0.5)
        labels = LabelSet(x='x', y='y', text='names', level='glyph', source=source_data, render_mode='canvas')
        self.figure.add_layout(labels)

    @staticmethod
    def create_table(source_data):
        columns = [
            TableColumn(field="x", title="X"),
            TableColumn(field="y", title="Y"),
            TableColumn(field="names", title="Name"),
            ]
        data_table = DataTable(source=source_data, columns=columns, width=400, height=280)
        return data_table

doc = curdoc()

@gen.coroutine
def update(data):
    source.data = data

def fetch_new_data(data):
    while True:
        # do some blocking computation
        sleep(0.5)
        data['y'][0] -= 0.1
        data['y'][1] -= 0.1
        data['y'][2] -= 0.1

        # but update the document from callback
        doc.add_next_tick_callback(partial(update, data))

def change_color(data_button):
    data_button['color'][0] = random.choice(["yellow", "red"])
    data_button['color'][1] = random.choice(["green", "red"])
    data_button['color'][2] = random.choice(["navy", "red"])
    doc.add_next_tick_callback(partial(update, data_button))

data = dict(
    x=[-1, 0, 1],
    y=[1.5, 2, 1.5],
    names=["Tocho", "Muy tocho", "No tan tocho"],
    color=["yellow", "yellow", "yellow"]
)
source = ColumnDataSource(data)

drawer = Drawer()
drawer.create_labeled_circles(source)
table = drawer.create_table(source)

button_1 = Button(label="Change color")
button_1.on_click(partial(change_color, data_button=data))

doc.add_root(row(drawer.figure, widgetbox(button_1, table)))

thread = Thread(target=fetch_new_data, args=(data,))
thread.start()

