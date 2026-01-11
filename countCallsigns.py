# What is the address of the ADS-B transponder using highest amount of distinct callsigns?
# 4896098
# And how many are we talking about (not including "nan")?
# 4

# Why is the number of distinct callsigns different from the number of distinct addresses?
# ICAO addresses identify aircraft, while callsigns identify flights and may change or be missing

import csv
from collections import defaultdict

filename = "./ex4_df/exercise_flights_subset.csv"  # File name

# Map address (col 1) -> set of callsigns (col 4)
addr_calls = defaultdict(set)

with open(filename, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        if not row:
            continue
        addr = row[1].strip()
        callsign = row[4].strip() if len(row) > 4 else ""
        if addr:
            addr_calls[addr].add(callsign)

# Sort addresses by number of unique callsigns (descending)
sorted_addrs = sorted(addr_calls.items(), key=lambda kv: len(kv[1]), reverse=True)

out_filename = "address_callsigns.tsv"
with open(out_filename, "w", encoding="utf-8") as out:
    out.write("address\tunique_callsigns_count\tcallsigns\n")
    for addr, calls in sorted_addrs:
        calls_str = ",".join(sorted(calls))
        out.write(f"{addr}\t{len(calls)}\t{calls_str}\n")

# Print a top-20 preview to the console
print("Top 20 addresses by number of unique callsigns:")
for addr, calls in sorted_addrs[:20]:
    print(f"{addr:>10}  {len(calls):3}  {', '.join(sorted(calls))}")

print(f"\nFull results written to {out_filename}")
