from CTile import Tile
from CBoard import Board
import tiles

# 1) take a tile from the pot, remove it from the original
# 2) check if it fits (we will go from top left to bottom right corner) => all sides corespond to the tiles around this one 
# 3) IF YES: increment index and repeat 
# 4) IF NO: turn 4 times, if still not insert into pot used and take another tile 
# 5) once it does fit, merge the regular pot with the ones used and repeat whole again

while True:
    
    tile = tiles.pot.pop()