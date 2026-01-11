# How many distinct ADS-B transponder addresses exist in in the data set?
# answer: 952

import csv
from collections import Counter

filename = "./ex4_df/exercise_flights_subset.csv"  # File name
fields = []  # Column names
rows = []  # Data rows

with open(filename, "r") as csvfile:
    csvreader = csv.reader(csvfile)  # Reader object

    fields = next(csvreader)  # Read header
    for row in csvreader:  # Read rows
        rows.append(row)

countedList = Counter(row[1] for row in rows)
print(len(countedList.keys()))
