# -*- coding: utf-8 -*-

"""Main module."""

from time import sleep
from threading import Thread
from functools import partial

from tornado import gen
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import DataTable, TableColumn, Button

class ObjectViewer:
    """ Object renderer"""

    def __init__(self):
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None,
                             title="Live object positions monitor")

    def create_circles(self, source_data):
        self.figure.circle(x='x', y='y', source=source_data, size=20, color="olive", alpha=0.5)
        labels = LabelSet(x='x', y='y', text='names', level='glyph', source=source_data, render_mode='css')
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

data = dict(
    x=[-1, 0, 1],
    y=[1.5, 2, 1.5],
    names=["Juan", "Carlos", "Baby"]
)
source = ColumnDataSource(data)

viewer = ObjectViewer()
viewer.create_circles(source)
table = viewer.create_table(source)

button_1 = Button(label="Start")
doc.add_root(row(viewer.figure, widgetbox(button_1, table)))

thread = Thread(target=fetch_new_data, args=(data,))
thread.start()

