from player import Player

class Game:
    def __init__(self):
        self.player1 = Player()
        self.player2 = Player()
        self.line_break = "*************************************************************************"


#Very first function to get called, It will either continue to call the run_game function or it will let the user exit.    
    def display_welcome(self):
        user_input = input("Welcome, would you like to play a game of battleship?\nYes/No : ").upper()
        if user_input == "YES":
            print("\n\nLet's sink some ships!")
            self.run_game()

#this will be our master function that will run out of the display welcome depending on what the user inputs
    def run_game(self):
        self.update_player_names()
        
#function updates the players names at the start of the game.
    def update_player_names(self):
        self.player1.name = (f"{self.player1.name}1")
        self.player2.name = (f"{self.player2.name}2")

