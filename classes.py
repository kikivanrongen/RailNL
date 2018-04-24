class Station():
    def __init__(self, name, x, y, critical, connections, time):

        self.name = name
        self.x = x
        self.y = y
        self.critical = critical

class Connection(Station):
    def __init__(self, connection, time, critical):
        super(Connection, self, connection, time, critical).__init__():
            self.connection = connection
            self.time = time
            self.critical = critical

class Route():
    def __init__(self, location, past_stations, time, critical_connections):
        self.location = location
        self.past_stations = past_stations
        self.time = time
        self.critical_connections = critical_connections
