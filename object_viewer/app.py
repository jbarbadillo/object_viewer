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

    def __init__(self):
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None)
        self.figure.border_fill_color = 'black'

        self.circle_renderer = self.figure.circle(x='x', y='y', size=20, color="olive", alpha=0.5)
        self.source = self.circle_renderer.data_source

    def callback(self, new_data):
        self.source.data = new_data


print("Started Object viewer {}".format(__version__ ))

# TODO: create datasource and add callback on data source change

viewer = ObjectViewer()

data = dict(
    x=[1, 2, 0],
    y=[1, 2, 1]
)
source = ColumnDataSource(data)
force_change = CustomJS(args=dict(source=source), code="""
    source.change.emit()
""")
source.js_on_change('data', force_change)

curdoc().add_root(row(viewer.figure))
