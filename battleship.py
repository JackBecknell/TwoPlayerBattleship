from ship import Ship

class Battleship(Ship):
    def __init__(self):
        self.length_positions = 4
        self.name = 'Battleship'
        super().__init__()
