# This file holds the global variables used in different modules

# 2D array for the game board itself
Board = [["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"],["----", "----", "----", "----"]]

# 1D arrays for storing available pieces and positions
LeftPieces = ["LHSN","LHCN","LTSN","LTCN","LHSY","LHCY","LTSY","LTCY","DHSN","DHCN","DTSN","DTCN","DHSY","DHCY","DTSY","DTCY"]
AvailableCoordinates = ["A1", "A2", "A3", "A4", "B1", "B2", "B3", "B4", "C1", "C2", "C3", "C4", "D1", "D2", "D3", "D4"]

# Status used as a flag to end the game, as well as track who won:
# 0 - on-going, 1 - Player1 won, 2 - Player2 won, 3 - it's a draw
Status = 0
