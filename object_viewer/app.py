# -*- coding: utf-8 -*-

"""Main module."""

from object_viewer.__init__ import __version__
from bokeh.plotting import figure, output_file, show, hplot
from bokeh import models

def render_plot(circle_x, circle_y, square_x, square_y):
    p.circle_x(circle_x, circle_y, size=20, color="navy", alpha=0.5)
    p.square(square_x, square_y, size=20, color="olive", alpha=0.5)

    # show the results
    show(p)

class ObjectViewer:
    def __init__(self):
        self.coords = {}
        self.graph_fig = None
        self.graph_plot = None
        self._display_graph()

        # self.graph_plot.data_source.on_change('selected', self.graph_update)

    def create_page(self):
        show(hplot(self.graph_fig))
        return

    def _display_graph(self):
        # Generate source
        graph_source = models.ColumnDataSource(self.coords)
        # Create figure
        self.graph_fig = figure(title='2d map', tools='pan,box_zoom,box_select,reset')
        
        # Create plot
        self.graph_plot = self.graph_fig.scatter('x', 'y', source=graph_source, color='color', alpha=0.6)
        return

if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))

    # output to static HTML file
    output_file("line.html")

    p = figure(plot_width=400, plot_height=400)

    circle_x = [1, 2]
    circle_y = [6, 7]
    square_x = [1, 2]
    square_y = [6.1, 7.1]
    
    viewer = ObjectViewer()



    