import csv
import classes.classes
import loading.load

# import data
# station_list = loading.load.stations("data/StationsHolland.csv")
# connection_list = loading.load.railroads("data/ConnectiesHolland.csv")

# put data in classes
# for element in station_list:
#     element[0] = classes.classes.Station(name=element[0], x=element[1],
#     y=element[2], critical = element[3])
    # classes.classes.Station(element)

NZ_Holland = classes.classes.Stations()
NZ_Holland.stations("data/StationsHolland.csv")
print(NZ_Holland.names)
