#!/usr/bin/env python3
import csv

OS = [["Mac OS", "11.0"],
      ["Windows", "11"],
      ["Android", "12"],
      ["Linux", "21.1"]]

# This will write to the CSV file
with open("os.txt", "w", newline="") as file:
    writer = csv.writer(file, delimiter="|")
    writer.writerows(OS)

# This will read the CSV file
with open("os.txt", newline="") as file:
    reader = csv.reader(file, delimiter="|")
    for row in reader:
        print(row[0], row[1])
