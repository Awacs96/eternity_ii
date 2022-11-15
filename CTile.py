# Class handling tiles

class Tile:

    def __init__(self, name, top, left, right, bottom):
        self.name = name
        self.top = top
        self.left = left
        self.right = right
        self.bottom = bottom
    
    def rotate(self):
        self.top, self.left, self.right, self.bottom = self.left, self.right, self.bottom, self.top

    def display(self):
        print(f"A: {self.top}, B: {self.left}, C: {self.right}, D: {self.bottom}")


# t = Tile("Ashley", None, None, None, None)
# t.display()