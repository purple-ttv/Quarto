# This file was written by Vakaris

# --- Importing all modules ---
# import time
import globals
from Greeting import OutputGreeting
from ShowBoard import ShowBoard
from LeftPieces import UpdatePieceList
from TakeFirstInput import TakeFirstInput
# from PlacePiece import PlacePiece
from PieceInput import TakePieceInput
# from CheckBoard import CheckBoard
from Ending import Ending
from ResolveStatus import ResolveStatus


# --- MAIN ---
# Showing a greeting message before the game starts
OutputGreeting()

# Board is shown for the first player
ShowBoard()

# Counter to track the move number is initialized
Counter = 0

# Player one chooses his first piece
Piece = TakeFirstInput()

while (globals.Status == 0):
    Counter += 1
    PlacePiece(Piece)   # Player places the given piece
    ShowBoard()         # Updated board is shown
    Piece = TakePieceInput()  # Player either piece for opponent or says "Quarto"  
    while (Piece == "Quatro"):
        if (CheckBoard()):
            ResolveStatus()
        else:
            print("There was no Quarto!")
            Piece = TakePieceInput()

    UpdatePieceList(Piece)

    if (globals.Status == 0) and (Counter == 16):
        globals.Status = 3

# PlacePiece is called, user makes position choice, board is updated

# In loop, players choose their piece from a possible list
Piece = TakePieceInput()

# PlacePiece is called and board updated and checked

# Finally, when game is over, a final message is output:
Ending(globals.Status)
# Player who won or that it was a draw
