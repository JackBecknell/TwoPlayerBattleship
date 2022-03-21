from ship import Ship

class Submarine(Ship):
    def __init__(self):
        self.length_positions = 3
        self.name = "Submarine"
        super().__init__()