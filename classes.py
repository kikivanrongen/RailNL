class Station():
    def __init__(self, name, x, y, critical):
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
    def __init__(self, stations, time, critical_connections):
        self.stations = stations
        self.time = time
        self.critical_connections = critical_connections