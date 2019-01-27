# -*- coding: utf-8 -*-

"""Main module."""

from object_viewer.__init__ import __version__
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

def render_plot(circle_x, circle_y, square_x, square_y):
    p.circle_x(circle_x, circle_y, size=20, color="navy", alpha=0.5)
    p.square(square_x, square_y, size=20, color="olive", alpha=0.5)

    # show the results
    show(p)

class ObjectViewer:
    def __init__(self):
        self.coords = {} # generate data with pandas cols?
        self.figure = None
        self.graph_plot = None
        self._display_graph()

        # self.graph_plot.data_source.on_change('selected', self.graph_update)

    def create_page(self):
        show(self.figure)
        return

    def _display_graph(self):
        # Generate source
        data = {'x': [1, 2, 3, 4, 5],
                'y': [6, 7, 2, 3, 6]}

        graph_source = ColumnDataSource(data)
        # Create figure
        self.figure = figure(title='2d map', tools='pan,box_zoom,box_select,reset', plot_width=800, plot_height=800)
        
        # Create plot
        self.graph_plot = self.figure.circle('x', 'y', source=graph_source, size=20, color='navy', alpha=0.6)
        return

if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))

    # output to static HTML file
    output_file("line.html")    

    circle_x = [1, 2]
    circle_y = [6, 7]
    square_x = [1, 2]
    square_y = [6.1, 7.1]
    
    viewer = ObjectViewer()
    viewer.create_page()



    