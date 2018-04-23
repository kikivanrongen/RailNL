import classes
import csv

with open("StationsHolland.csv", newline= " ") as csvfile:
    stations = csv.DictReader(csvfile)

with open("ConnectionsHolland.csv", newline = " ") as csvfile:
    connections = csv.DictReader(csvfile)