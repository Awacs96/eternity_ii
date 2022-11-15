# Classes for handling tiles and board

class Tile:

    def __init__(self, number, top, left, right, bottom):
        self.number = number
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom
    

class Board:

    def __init__(self, size=4):
        self.board = []
        self.size = size

        for i in range(self.size + 2):
            for j in range(self.size + 2):
                if i == 0 or i == self.size + 1 or j == 0 or j == self.size + 1:
                    self.board.append([Tile("outside", 0, 0, 0, 0)])
                else:
                    self.board.append([Tile("inside", 1, 1, 1, 1)])


    def display(self):

        for i in range(self.size + 2):
            row = ""
            for j in range(self.size + 2):
                row += self.board[i][j].number
            print(row)


#       print((self.board[0][0]).number)

