# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:38:11 2017

@author: syl
"""
import csv
import io
import json


def csv_to_json(path):  # pragma: no cover
    """
    Convert the csv file into a json file while removing '/uFEFF' unicode character for space

    :param path: path of the csv file
    :return: print the json folder with same name in same directory
    """
    with io.open(path, 'r', encoding='utf8') as f:
        reader = csv.DictReader((x.replace(u"\uFEFF", u"") for x in f))
        rows = list(reader)

    with open(path[:-3] + "json", 'w', encoding='utf8') as f:
        f.write(json.dumps(rows, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False))


def conversion(path, delim):
    """
    Convert a csv file input into a truth.json file and a dare.json file
    To work with the truth or dare app.

    """
    csv_truth = []
    csv_dare = []

    try:
        # Conversion csv to json
        with open(path, "rt") as csv_file:
            reader = csv.reader(csv_file, delimiter=delim, quoting=csv.QUOTE_ALL)
            fieldnames = next(reader)
            reader = csv.DictReader(csv_file, delimiter=delim, fieldnames=fieldnames)
            for row in reader:
                if row["type"] == "Truth":
                    csv_truth.append(row)
                elif row["type"] == "Dare":
                    csv_dare.append(row)

            csv_to_json.to_json("truth.json", csv_truth)
            csv_to_json.to_json("dare.json", csv_dare)

    except FileNotFoundError:
        print(path + " was not found")


def main():
    """
    Script for truth or dare app

    """
    conversion("input.csv", ";")


if __name__ == '__main__':
    main()
