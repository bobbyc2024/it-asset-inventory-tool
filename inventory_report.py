import csv

filename = "sample_assets.csv"

with open(filename, newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    devices = list(reader)

print(f"Total devices: {len(devices)}")
