# -*- coding: utf-8 -*-

"""Main module."""

from time import sleep
from bokeh.plotting import figure, output_file, show, curdoc
from bokeh.models import ColumnDataSource

from object_viewer.__init__ import __version__

class ObjectViewer:
    """ Object renderer"""

    def __init__(self):
        self.data = {'x': [],
                     'y': [],
                     'uid': []} # generate data with pandas cols?
        self.graph_source = None
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None)
        self.figure.border_fill_color = 'black'
        self.graph_plot = None
        self._display_graph()

        # self.graph_plot.data_source.on_change('selected', self.graph_update)

    def create_page(self):
        show(self.figure)

    def _display_graph(self):
        # TODO: generate source using pandas and injecting data every second

        self.graph_source = ColumnDataSource(self.data)


        # Create plot
        self.graph_plot = self.figure.circle('x', 'y', source=self.graph_source, size=20, color='navy', alpha=0.6,
                                             line_color="#3288bd", line_width=3)

    def update_source(self, new_data):
        self.graph_source = ColumnDataSource(new_data)
        self.graph_plot = self.figure.circle('x', 'y', source=self.graph_source, size=20, color='navy', alpha=0.6,
                                             line_color="#3288bd", line_width=3)

if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))



    viewer = ObjectViewer()
    data = {'x': [1],
            'y': [1],
            'uid': [1]}
    viewer.update_source(data)
    viewer.create_page()

    sleep(1)
    data = {'x': [1],
            'y': [1.1],
            'uid': [1]}
    viewer.update_source(data)
