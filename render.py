#!/usr/bin/env python3

import json
import locale
import glob
import os

from staticjinja import Site


def format_price(value):
    if value is None or not isinstance(value, int):
        return value
    formatted_price = "{:,d}".format(value).replace(",", " ")
    return formatted_price


filters = {
    'format_price': format_price,
}


def collect_data_filepaths(directory_path='data', ):
    for file in os.listdir(directory_path):
        if file.endswith(".json"):
            yield os.path.join(directory_path, file)


if __name__ == "__main__":
    locale.setlocale(locale.LC_ALL, '')

    data_filepaths = list(collect_data_filepaths())

    cars = []
    for filename in data_filepaths:
        with open(filename, 'r') as file:
            site_cars = json.loads(file.read())
            cars.extend(site_cars)

    site = Site.make_site(env_globals={
        'cars': cars,
    }, filters=filters)

    site.render(use_reloader=True)
