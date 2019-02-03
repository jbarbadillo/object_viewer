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
from bokeh.models.widgets import DataTable, TableColumn, Button, NumberFormatter

doc = curdoc()

class Drawer:
    """ Object drawer"""

    def __init__(self, source):
        self.source = source
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None,
                             title="Live object positions monitor")

    def create_labeled_circles(self):
        """ Creates circles representation for a given data source """
        self.figure.circle(x='x', y='y', source=self.source, size=20, color="color", alpha=0.5)
        labels = LabelSet(x='x', y='y', x_offset=20, text='names', level='glyph', source=self.source,
                          render_mode='canvas')
        self.figure.add_layout(labels)

    @staticmethod
    def create_table(source_data):
        """ Creates a table from the source data """
        decimal_formatter = NumberFormatter(format='0.0')
        columns = [
            TableColumn(field="x", title="X", formatter=decimal_formatter),
            TableColumn(field="y", title="Y", formatter=decimal_formatter),
            TableColumn(field="names", title="Name"),
            TableColumn(field="color", title="Color"),
            ]
        data_table = DataTable(source=source_data, columns=columns, width=400, height=280)
        return data_table

    @gen.coroutine
    def update_data(self, new_data):
        """ Updates source with new data """
        self.source.data = new_data

    def start_fetching_data(self, new_data):
        """ Method that simulates fetching new data and updating """
        while True:
            # do some blocking computation
            sleep(0.5)
            new_data['y'][0] -= 0.1
            new_data['y'][1] -= 0.1
            new_data['y'][2] -= 0.1

            # but update the document from callback
            doc.add_next_tick_callback(partial(self.update_data, new_data))

    def change_color(self, data_button):
        """ Changes data color and calls update_data """
        data_button['color'][0] = random.choice(["yellow", "red"])
        data_button['color'][1] = random.choice(["green", "red"])
        data_button['color'][2] = random.choice(["navy", "red"])
        doc.add_next_tick_callback(partial(self.update_data, data_button))


def initialize_source():
    fake_data = dict(
        x=[-1, 0, 1],
        y=[1.5, 2, 1.5],
        names=["Tocho", "Muy tocho", "No tan tocho"],
        ids=["111", "222", "333"],
        color=["yellow", "yellow", "yellow"]
    )
    data_source = ColumnDataSource(fake_data)
    return data_source, fake_data

source, data = initialize_source()
drawer = Drawer(source)
drawer.create_labeled_circles()
table = drawer.create_table(source)

button_1 = Button(label="Change color")
button_1.on_click(partial(drawer.change_color, data_button=data))

doc.add_root(row(drawer.figure, widgetbox(button_1, table)))

thread = Thread(target=drawer.start_fetching_data, args=(data,))
thread.start()

