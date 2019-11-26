# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 06:34:29 2016

@Docs: https://docs.scipy.org/doc/numpy/reference/generated/numpy.arange.html
@Docs: http://matplotlib.org/examples/pylab_examples/date_demo_convert.html

@author: sylhare
"""
# import sys
import csv
# from matplotlib.dates import DayLocator, HourLocator
import datetime
import io
# import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from matplotlib.dates import DateFormatter

# -- WRITE CSV -- #
c = csv.writer(open("test.csv", "wt"))  # wt write in text mode
c.writerow(["Date", "Money", "Types", "Other"])
date = ['2016/11/20', '2016/11/22', '2016/11/24', '2016/11/24', '2016/11/26',
        '2016/11/28']
money = [1, 12, 3, 5, 3, 2]
types = ['B', 'B', 'B', 'B', 'B', 'B']
other = ['A', 'A', 'A', 'A', 'A', 'A']

for i in range(0, len(date)):
    c.writerow([date[i], money[i], types[i], other[i]])

# -- READ CSV -- #
# f = open(sys.argv[1], 'rt') #Will open file when running python CSV_Handler.py file.csv
# try:
#    reader = csv.reader(f)
#    for row in reader:
#        print (row)
# finally:
#    f.close()


with open("test.csv", "rt") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
    fieldnames = next(reader)
    # reader = csv.DictReader(csvfile, delimiter=';', fieldnames=fieldnames)
    for row in reader:
        for i in range(len(row)):
            print(fieldnames[i] + ":" + row[i])
        for r in row:
            print(r)

columns = defaultdict(list)  # each value in each column is appended to a list
with open("test.csv", "rt") as f:
    reader = csv.DictReader(f)  # read rows into a dictionary format
    for row in reader:  # read a row as {column1: value1, column2: value2,...}
        for (k, v) in row.items():  # go over each column name and value
            columns[k].append(v)  # append the value into the appropriate list
            # based on column name k

with io.open("test.csv", 'r', encoding='utf-8', newline='') as f:
    sniffer = csv.Sniffer()
    dialect = sniffer.sniff(f.readline(), [',', ';'])  # Check for the delimiter
    f.seek(0)  # Go back at the beginning of the file

    # reader = csv.reader(map(lambda x: x.replace(u"\uFEFF", u""), f), dialect)
    reader = csv.reader((x.replace(u"\uFEFF", u"") for x in f), dialect)

    rows = list(reader)

# -- WORK WITH CSD DATA -- #
dates = columns['Date']
money = columns['Money']
types = columns['type']

dates = [datetime.datetime.strptime(date, '%Y/%m/%d') for date in dates]
# date = [date.weekday() for date in dates]
datetime.datetime.today().weekday()  # 0 is Monday, 6 is Sunday

# y = np.arange(len(dates)*1.0) #np.ranage return evenly spaced values within a given interval.
fig, ax = plt.subplots()
ax.plot_date(dates, money)
ax.hist(dates, bins=10, color='lightblue')

# ax.xaxis.set_major_locator(DayLocator())
# ax.xaxis.set_minor_locator(HourLocator(np.arange(0, 25, 6)))
ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
# ax.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
fig.autofmt_xdate()  # Put the dates in a good format (visible not next to each other)

plt.show()
plt.figure()
plt.plot(columns['Money'])
