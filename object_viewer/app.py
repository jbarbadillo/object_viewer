# -*- coding: utf-8 -*-

"""Main module."""

from time import sleep
from threading import Thread
from functools import partial
import random

from tornado import gen
from bokeh.plotting import figure, curdoc
from bokeh.models import ColumnDataSource, LabelSet
from bokeh.layouts import row, widgetbox
from bokeh.models.widgets import DataTable, TableColumn, Button, NumberFormatter

doc = curdoc()

class Drawer:
    """ Object drawer"""

    def __init__(self, people_source, phones_source):
        self.people_source = people_source
        self.phones_source = phones_source
        self.figure = figure(x_range=(-2, 2), y_range=(-2, 2), toolbar_location=None,
                             title="Live object positions monitor")

    def create_labeled_circles(self):
        """ Creates circles representation for a given data source """
        self.figure.circle(x='x', y='y', source=self.people_source, size=20, color="color", alpha=0.5)
        labels = LabelSet(x='x', y='y', x_offset=20, text='names', level='glyph', source=self.people_source,
                          render_mode='canvas')
        self.figure.add_layout(labels)

    def create_labeled_squares(self):
        """ Creates squares representation for a given data source """
        self.figure.square(x='x', y='y', source=self.phones_source, size=20, color="color", alpha=0.5)
        labels = LabelSet(x='x', y='y', x_offset=-40, text='names', level='glyph', source=self.phones_source,
                          render_mode='canvas')
        self.figure.add_layout(labels)

    @staticmethod
    def create_table(source_data):
        """ Creates a table from the source data """
        decimal_formatter = NumberFormatter(format='0.0')
        columns = [
            TableColumn(field="ids", title="Id"),
            TableColumn(field="x", title="X", formatter=decimal_formatter),
            TableColumn(field="y", title="Y", formatter=decimal_formatter),
            TableColumn(field="names", title="Name"),
            TableColumn(field="phones", title="Phone"),
            TableColumn(field="color", title="Color"),
            ]
        data_table = DataTable(source=source_data, columns=columns, width=400, height=280)
        return data_table

    @gen.coroutine
    def update_data(self, people_data, phones_data):
        """ Updates source with new data """
        self.people_source.data = people_data

        if phones_data:
            self.phones_source.data = phones_data

    def start_fetching_data(self, new_people, new_phones):
        """ Method that simulates fetching new data and updating """
        while True:
            # do some blocking computation
            sleep(0.5)
            for i in range(0, len(new_people['y'])):
                new_people['y'][i] -= 0.1

            for i in range(0, len(new_phones['y'])):
                new_phones['y'][i] -= 0.1

            # but update the document from callback
            doc.add_next_tick_callback(partial(self.update_data, new_people, new_phones))

    def change_color(self, data_button):
        """ Changes data color and calls update_data """
        data_button['color'][0] = random.choice(["yellow", "red"])
        data_button['color'][1] = random.choice(["green", "red"])
        data_button['color'][2] = random.choice(["navy", "red"])
        doc.add_next_tick_callback(partial(self.update_data, data_button, None))


def initialize_people_source():
    """ Generates a initial source for people data """
    fake_data = dict(
        x=[-1, 0, 1],
        y=[1.5, 2, 1.5],
        names=["Tocho", "Muy tocho", "No tan tocho"],
        phones=["-", "-", "-"],
        ids=["111", "222", "333"],
        color=["yellow", "yellow", "yellow"]
    )
    data_source = ColumnDataSource(fake_data)
    return data_source, fake_data

def initialize_phone_source():
    """ Generates a initial source for phone data """
    fake_data = dict(
        x=[-1.1, 1.1],
        y=[1.5, 1.5],
        names=["xiaomi", "bq"],
        ids=["111", "333"],
        color=["gray", "gray"]
    )
    data_source = ColumnDataSource(fake_data)
    return data_source, fake_data

def find_phone(p_id, phone_data):
    """ Finds the phone corresponding to the given user id """

    if p_id in phone_data['ids']:
        position = phone_data['ids'].index(p_id)
        return phone_data['names'][position]

    return "-"

def update_with_phone_info(people_data, phone_data):
    """ Updates people data with phone information, if available """
    for p_id in people_data["ids"]:
        phone = find_phone(p_id, phone_data)
        pos = people_data['ids'].index(p_id)
        people_data["phones"][pos] = phone

    return ColumnDataSource(people_data)

def main():
    """ Bokeh server main method """

    source_a, data_a = initialize_people_source()
    source_b, data_b = initialize_phone_source()
    source_a = update_with_phone_info(data_a, data_b)

    drawer = Drawer(source_a, source_b)
    drawer.create_labeled_circles()
    drawer.create_labeled_squares()
    table = drawer.create_table(source_a)

    button_change_color = Button(label="Change color")
    button_change_color.on_click(partial(drawer.change_color, data_button=data_a))

    doc.add_root(row(drawer.figure, widgetbox(button_change_color, table)))

    thread = Thread(target=drawer.start_fetching_data, args=(data_a, data_b))
    thread.start()

main()
