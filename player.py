from board import Board
from submarine import Submarine
from destroyer import Destroyer
from aircraft_carrier import AircraftCarrier
from battleship import Battleship

class Player:
    def __init__(self):
        self.name = 'Player'
        self.player_board = Board()
        self.submarine = Submarine()
        self.destroyer = Destroyer()
        self.battleship1 = Battleship()
        self.battleship2 = Battleship()
        self.aircraft_carrier = AircraftCarrier()

#The function that is called to place a ship, within is included all necesary funcion calls for placing a ship.
    def player_places_ship(self):
        pass


#The function that is called to set a starting grid for a ship
    def player_selects_starting_grid(self):
        self.player_board.display_board()
        letter = self.player_selects_letter_for_ship_placement()
        number = self.player_selects_number_for_ship_placement()
        self.ship_start_point_placement(letter, number)
        direction_for_rest_of_ship = input(f"Next, Using 'North', 'South', 'East', or 'West. type the direction you want the remaining length of your ship to fall.\n : ")


#Once player places ship works then work on this
    def ship_start_point_placement(self, pass_grid):
        if pass_grid in self.player_board:
            print('works')
        else:
            print('Damn it all')






