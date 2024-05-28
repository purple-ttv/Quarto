# This file was written by Vakaris

# --- Importing all modules ---
import time
import globals
from Greeting import OutputGreeting
from ShowBoard import ShowBoard
from LeftPieces import UpdatePieceList
from TakeFirstInput import TakeFirstInput
from MovePrompt import WhoseMove
from PlacePiece import PlacePiece
from PieceInput import TakePieceInput
from CheckBoard import CheckBoard
from Ending import Ending
from ResolveStatus import ResolveStatus


# --- MAIN ---

print("You chose to play PvP (Person versus Person)")

ShowBoard()                     # The board is shown for the first player

Counter = 0                     # Counter to track the move number
IsOver = False                  # Flag used to break out of the main loop

WhoseMove(1)                    # Prompt to show it's Player 1's move
Piece = TakeFirstInput()        # Player one chooses his first piece
                                # Different function, as player can choose a piece himself

while (globals.Status == 0):    # Loop will stop when the global Status variable is changed (indicating the ste of the game)
    Counter += 1
    if (Counter != 1):          # Skipping the first counter to avoid prompting twice
        WhoseMove(Counter)      # Prompt that shows whose move it is
    PlacePiece(Piece)           # Player places the given piece
    ShowBoard()                 # Updated board is shown

    if (globals.Status == 0) and (Counter == 16):
        globals.Status = 3      # To indicate a draw ("and" needed to avoid a problem when a player wins on last move)
        break                   # Loop needs to end before taking another piece input, as no more pieces left in a draw
    
    Piece = TakePieceInput()    # Player either chooses a piece for opponent or says "Quarto" if he believes he can win
    while (Piece == "Quarto"):
        if (CheckBoard()):      # If a Quarto is present on the board, the current player wins, else play continues
            ResolveStatus(Counter)
            IsOver = True
            break               # Needed as value of Piece doesn't actually change, i.e. loop wouldn't be exited
        else:                   # I.e. player called Quarto incorrectly, play proceeds after player enters a valid piece
            print("There was no Quarto!")
            Piece = TakePieceInput()

    if IsOver == True:
        break                   # Loop is exited fully in case game finished

    UpdatePieceList(Piece)      # Only executed when Piece is for sure on the LeftPieces list (previous loop ensures this)

Ending(globals.Status)          # Finally, when game is over, a final message is output based on the result
