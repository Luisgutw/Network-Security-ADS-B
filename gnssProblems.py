# In the data set you will find four flights with ongoing GNSS problems that may be related to jamming. Name the callsigns of those flights. Fill in the blanks in alphabetical order!
# There are 4 flights

# 1. GAFTT18 (NIC immer 0 -> kein GNSS-Signal bei 1439 Datenpunkten)
# 2. AUA962 (Counter({'AUA962_0': 252, 'AUA962_3': 1}))
# 3. MGL137 (Counter({'MGL137_0': 233}))
# 4. UZB211 (Counter({'UZB211_0': 23}))

# 1. AUA962
# 2. GAFTT18
# 3. MGL137
# 4. UZB211

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

# flights_with_bad_nic = []
# for row in rows:
#     if int(row[11]) < 4 and row[4] == "UZB211":
#         flights_with_bad_nic.append(row[4] + "_" + row[11])

# countedList = Counter(flights_with_bad_nic)
# print("Flights with bad NIC:", flights_with_bad_nic)
# print("Distinct callsigns with bad NIC:", countedList)
# print("Number of data points from aircraft with bad NIC:", len(flights_with_bad_nic))


flights_with_bad_nic = []
for row in rows:
    if int(row[3]) == 0 or int(row[6]) == 0:
        continue
    if int(row[3]) / int(row[6]) < 0.3 or int(row[3]) / int(row[6]) > 3:
        flights_with_bad_nic.append(row[4])
        print(
            f"Row with GNSS problem: Callsign={row[4]}, Barometric Height={row[3]}, Geometric Height={row[6]}, Ratio={int(row[3]) / int(row[6]):.2f}"
        )
