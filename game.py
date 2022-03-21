from random import randint
from player import Player
class Game:
    def __init__(self):
        self.player_one = Player()
        self.player_one.name = 'Player 1'
        self.player_two = Player()
        self.player_two.name = 'Player 2'

#Should rethink this function. Try to set on master function call to iterate through only function calls needed to run the game.
#
    def start_game(self):
        play_or_leave = self.welcome_message()
        if play_or_leave == True:
            who_goes_first = self.coin_toss()
            if who_goes_first == True:
                self.ship_placement_message(self.player_one)
                self.show_board_for_placement(self.player_one)
            else:
                self.ship_placement_message(self.player_two)
                self.show_board_for_placement(self.player_two)
        else:
            print('Have a nice day!')

#A function called at the beginning of the game that randomizes who gets to go first.
    def coin_toss(self):
        random_num = randint(1,2)
        if randint == 1:
            return True
        else:
            return False

#Allows player to choose whether they want to play or not.
    def welcome_message(self):
        user_chooses_to_play = input("""Welcome to TWO PLAYER BATTLESHIP. Do you want to play a game?(Y/N) : """).upper()
        while user_chooses_to_play:
            if user_chooses_to_play == 'Y' or user_chooses_to_play == 'YES':
                return True
            elif user_chooses_to_play == 'N' or user_chooses_to_play == 'NO':
                return False
            else:
                user_chooses_to_play = input("""Sorry, that command isn't recognized.\nType 'Yes' to play or 'No' to quit.\n : """)

    def ship_placement_message(self, player):
        print(f"""Alright {player.name}, it's your turn to place your ships. We will be playing with traditional battleship rules.
        You have a total of 5 ships to be placed on your board.
        -1 Destroyer (Unit length of 2).
        -1 Submarine (Unit length of 3).
        -2 Battlships (Unit length of 4).
        -1 Aircraft Carrier (Unit length of 5).
Once all ships have been placed there will be another coin toss to determine who gets to shoot first. Remember though, while placing
your ships they cannot overlap, or lead off of the board (which is a 20x20 grid). For reference here is your board.""")
        
    def show_board_for_placement(self, player):
        player.player_board.display_board()
        redisplay = input("If you hadn't expanded your terminal enough and are missing some rows type Type 'Yes'.\nOtherwise if you would like to continue Type 'No'\n : ").upper()
        if redisplay == 'YES' or redisplay == 'Y':
            player.player_board.display_board()
        
    