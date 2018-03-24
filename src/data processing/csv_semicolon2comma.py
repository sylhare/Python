import csv
# http://stackabuse.com/reading-and-writing-csv-files-in-python/

if __name__ == "__main__":  # pragma: no cover
    path = "test.csv"
    reader = csv.reader(open(path, "rU"), delimiter=',')
    writer = csv.writer(open("output.csv", 'w'), delimiter=';')  # quoting=csv.QUOTE_ALL for quoting
    writer.writerows(reader)

    #reader = list(csv.reader(open(path, "rU"), delimiter=','))
    #writer = csv.writer(open(path, 'w'), delimiter=';')
    #writer.writerows(row for row in reader)
    #with open(path, "w") as f:
    #    writer = csv.writer(f, delimiter=';')
    #    for row in reader:
    #        writer.writerow(row)

    with open('test.csv', 'rb') as csvfile:
        sniffer = csv.Sniffer()
        has_header = sniffer.has_header(csvfile.read(2048))
        print(has_header)
        csvfile.seek(0)
        print(csvfile.read(2048))
        csvfile.seek(0)
        reader = csv.reader(csvfile)
        print(reader)
        has_header = sniffer.has_header(csvfile.read(2048))
        print(has_header)


