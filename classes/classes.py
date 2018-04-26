import csv

class Stations():

    def __init__(self):

        self.names = []
        self.x = []
        self.y = []
        self.critical = []

    def stations(self, stations_csv):
        """returns list of all stations with
        corresponding coordinates"""

        # open csv file with stations
        with open (stations_csv) as file_stations:

            # read csv file and return list of columns
            read_stations = csv.DictReader(file_stations)

            # iterate over rows and append to class
            for row in read_stations:
                self.names.append(row[0])
                self.x.append(float(row[1]))
                self.y.append(float(row[2]))

                if row[3] == 'Kritiek':
                    self.critical.append(True)
                else:
                    self.critical.append(False)

# class Connection(Station):
#     def __init__(self, connection, time, critical):
#         super(Connection, self, connection, time, critical).__init__():
#             self.connection = connection
#             self.time = time
#             self.critical = critical
#
# class Route():
#     def __init__(self, location, past_stations, time, critical_connections):
#         self.location = location
#         self.past_stations = past_stations
#         self.time = time
#         self.critical_connections = critical_connections
