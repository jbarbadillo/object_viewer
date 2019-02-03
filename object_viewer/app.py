# -*- coding: utf-8 -*-

"""Main module."""

from time import sleep
from threading import Thread
from random import random
from functools import partial

from tornado import gen
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource
from bokeh.models.callbacks import CustomJS
from bokeh.layouts import row

from __init__ import __version__

class ObjectViewer:
    """ Object renderer"""

    def __init__(self, source_a):
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None)

        self.circle_renderer = self.figure.circle(x='x', y='y', source=source_a, size=20, color="olive", alpha=0.5)
        self.source = self.circle_renderer.data_source

    def callback(self, new_data):
        self.source.data = new_data

    def update_graph(self):
        print("shitty")


doc = curdoc()

data = dict(
    x=[1, 2, 0],
    y=[1, 2, 1]
)
source = ColumnDataSource(data)

@gen.coroutine
def update_graph(data):
    source.data = data

def update(data):
    while True:
        # do some blocking computation
        sleep(0.1)
        data['y'][0] -= 0.1
        data['y'][1] -= 0.1
        data['y'][2] -= 0.1

        # but update the document from callback
        doc.add_next_tick_callback(partial(update_graph, data))


viewer = ObjectViewer(source)

doc.add_root(row(viewer.figure))

thread = Thread(target=update, args=(data,))
thread.start()

