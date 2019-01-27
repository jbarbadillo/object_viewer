# -*- coding: utf-8 -*-

"""Main module."""

from object_viewer.__init__ import __version__
from bokeh.plotting import figure, output_file, show


if __name__ == "__main__":
    print("Started Object viewer {}".format(__version__ ))

    # output to static HTML file
    output_file("line.html")

    p = figure(plot_width=400, plot_height=400)

    # add a circle renderer with a size, color, and alpha
    p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
    p.square([1, 2, 3, 4, 5], [7, 8, 3, 5, 6], size=20, color="olive", alpha=0.5)


    # show the results
    show(p)