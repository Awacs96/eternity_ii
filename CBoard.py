# Class handling Board

from CTile import Tile

class Board:

    def __init__(self, size=16):
        self.board = []
        self.size = size

        for i in range(self.size + 2):
            for j in range(self.size + 2):
                if i == 0 or i == self.size + 1 or j == 0 or j == self.size + 1:
                    self.board.append(Tile("OUT", 0, 0, 0, 0))
                else:
                    self.board.append(Tile("IN", 1, 1, 1, 1))


    def insertTiles():
        pass


    def display(self):

        self.counter = 0
        self.rows = ""
        
        for tile in self.board:
            self.rows += tile.name
            self.counter += 1

            if self.counter % (self.size + 2) == 0:
                self.rows += "\n"
            else:
                self.rows += "\t"
        
        print(self.rows)


# b = Board()
# print(b.board[2].name)