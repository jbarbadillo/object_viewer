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

        self.circle_renderer = self.figure.circle(x='x', y='y', size=20, color="olive", alpha=0.5)
        self.source = self.circle_renderer.data_source

    def callback(self, new_data):
        self.source.data = new_data



if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))

    # TODO: create datasource and add callback on data source change

    viewer = ObjectViewer()


    curdoc().add_root(viewer.figure)
