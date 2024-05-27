# This file holds the global variables used in different modules

# 2D array for the game board itself
Board = [["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"]]

# 1D arrays for storing available pieces and positions
LeftPieces = ["LHSN","LHCN","LTSN","LTCN","LHSY","LHCY","LTSY","LTCY","DHSN","DHCN","DTSN","DTCN","DHSY","DHCY","DTSY","DTCY"]

# Status used as a flag to end the game, as well as track who won:
# 0 - on-going, 1 - Player1 won, 2 - Player2 won, 3 - it's a draw
Status = 0