from ship import Ship

class AircraftCarrier(Ship):
    def __init__(self):
        self.length_positions = 5
        self.name = 'Aircraft Carrier'
        super().__init__()