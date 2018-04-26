import csv
import classes.classes
import loading.load

# import data
station_list = loading.load.stations("data/StationsHolland.csv")
connection_list = loading.load.railroads("data/ConnectiesHolland.csv")

# put data in classes
for element in station_list:
    for (k, v) in element.items():
        print(v)
        s = classes.classes.Station(name=v[1], x=v[2], y=v[3], critical = v[4])
