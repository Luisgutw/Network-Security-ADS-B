# How many data points are there from aircraft on the ground?
# 23528

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

flights_on_ground = []
for row in rows:
    if row[5] == "True":
        flights_on_ground.append(row[1])
    # elif row[5] == "False" and row[1] in flights_on_ground:
    #     print("Error: Flight took off again:", row[1])

print("Flights on the ground:", flights_on_ground)
print("Number of data points from aircraft on the ground:", len(flights_on_ground))
