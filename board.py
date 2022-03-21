
class Board():
        def __init__(self):
            self.vertical_axis_num = 0
            self.horizontal_axis_letter = ''
            self.a_to_t = ['A', "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
            self.board = []
            self.create_ocean()

 #when this function runs it updates self.board into a full grid 20x20 with A-T (vert) and 1-20(horizontal)       
        def create_ocean(self):
            for i in range(20):
                self.board.insert(i, [])
                for j in range(20):
                    self.board[i] += [[self.a_to_t[i]+str(j+1)]]

#An incomplete function, need to update the elif evaluating for 1 len to see how this works when we replace the index with either a 'HIT' or part of a ship.
        def display_board(self):
            for i in self.board:
                print(i, end='\n')

        


