# -*- coding: utf-8 -*-

"""Main module."""

import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

from object_viewer.__init__ import __version__

class ObjectViewer:
    """ Object renderer"""

    def __init__(self):
        self.data = {'x': [],
                       'y': [],
                       'uid': []} # generate data with pandas cols?
        self.figure = None
        self.graph_plot = None
        self._display_graph()

        # self.graph_plot.data_source.on_change('selected', self.graph_update)

    def create_page(self):
        show(self.figure)

    def _display_graph(self):
        # TODO: generate source using pandas and injecting data every second

        graph_source = ColumnDataSource(self.data)
        # Create figure
        self.figure = figure(title='2d map',
                             tools='pan,box_zoom,box_select,reset',
                             plot_width=600,
                             plot_height=600)

        # Create plot
        self.graph_plot = self.figure.circle('x', 'y', source=graph_source, size=20, color='navy', alpha=0.6,
                                             line_color="#3288bd", line_width=3)

    def update_source(self, data):
        new_source = ColumnDataSource(data)
        self.graph_plot = self.figure.circle('x', 'y', source=new_source, size=20, color='navy', alpha=0.6,
                                             line_color="#3288bd", line_width=3)

if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))

    # output to static HTML file
    output_file("line.html")

    viewer = ObjectViewer()
    viewer.create_page()
