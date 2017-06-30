# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:38:11 2017

@author: syl
"""
import csv
import csv_to_json as ctj

def conversion(path, delim):
    """
    Convert a csv file input into a truth.json file and a dare.json file
    To work with the truth or dare app.

    """
    csv_truth = []
    csv_dare = []

    try:
        #Conversion csv to json
        with open(path,"rt") as csv_file:
            reader = csv.reader(csv_file, delimiter=delim, quoting=csv.QUOTE_ALL)
            fieldnames = next(reader)
            reader = csv.DictReader(csv_file, delimiter=delim, fieldnames=fieldnames)
            for row in reader:
                if row["type"] == "Truth":
                    csv_truth.append(row)
                elif row["type"] == "Dare":
                    csv_dare.append(row)

            ctj.to_json("truth.json", csv_truth)
            ctj.to_json("dare.json", csv_dare)

    except FileNotFoundError:
        print(path +" was not found")

def main():
    """
    Script for truth or dare app

    """
    conversion("input.csv",";")

if __name__ == '__main__':
    main()
