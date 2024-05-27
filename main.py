# This file was written by Vakaris

# --- Importing all modules ---
# import time
import globals
from Greeting import OutputGreeting
from ShowBoard import ShowBoard
# from LeftPieces import UpdatePieceList
from TakeFirstInput import TakeFirstInput
from PieceInput import TakePieceInput
from Ending import Ending


# --- MAIN ---
# Showing a greeting message before the game starts
OutputGreeting()

# Board is shown for the first player
ShowBoard()

# Player one chooses his first piece
Piece = TakeFirstInput()

# PlacePiece is called, user makes position choice, board is updated

# In loop, players choose their piece from a possible list
Piece = TakePieceInput()

# PlacePiece is called and board updated and checked

# Finally, when game is over, a final message is output:
Ending(globals.Status)
# Player who won or that it was a draw