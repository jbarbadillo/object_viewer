# -*- coding: utf-8 -*-

"""Main module."""

from time import sleep
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import ColumnDataSource

from object_viewer.__init__ import __version__

class ObjectViewer:
    """ Object renderer"""

    def __init__(self):
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None)
        self.figure.border_fill_color = 'black'

        # TODO: create glyph circle renderer
        self.circle_renderer = self.figure.circle()
        self.source = self.circle_renderer.data_source

        # TODO: create a callback


if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))



    viewer = ObjectViewer()
    data = {'x': [1],
            'y': [1],
            'uid': [1]}


    sleep(1)
    data = {'x': [1],
            'y': [1.1],
            'uid': [1]}
