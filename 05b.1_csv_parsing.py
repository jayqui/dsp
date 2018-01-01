import csv
with open("./python/faculty.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile)

    results = {}

    for row in spamreader:
        print(row[1])

