# -*- coding: utf-8 -*-

"""Main module."""

from object_viewer.__init__ import __version__
from bokeh.plotting import figure, output_file, show

def render_plot(circle_x, circle_y, square_x, square_y):
    p.circle_x(circle_x, circle_y, size=20, color="navy", alpha=0.5)
    p.square(square_x, square_y, size=20, color="olive", alpha=0.5)

    # show the results
    show(p)

if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))

    # output to static HTML file
    output_file("line.html")

    p = figure(plot_width=400, plot_height=400)

    circle_x = [1, 2]
    circle_y = [6, 7]
    square_x = [1, 2]
    square_y = [6.1, 7.1]
    
    render_plot(circle_x, circle_y, square_x, square_y)


    