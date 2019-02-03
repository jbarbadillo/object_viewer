# -*- coding: utf-8 -*-

"""Main module."""

from time import sleep
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

print("Started Object viewer {}".format(__version__ ))

# TODO: create datasource and add callback on data source change



data = dict(
    x=[1, 2, 0],
    y=[1, 2, 1]
)
source = ColumnDataSource(data)
force_change = CustomJS(args=dict(source=source), code="""
    source.change.emit()
""")
source.js_on_change('data', force_change)

viewer = ObjectViewer(source)

curdoc().add_root(row(viewer.figure))


