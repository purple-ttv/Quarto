# This file was written by Arsenii

# --- Importing all modules ---
import time
import random
import globals
from ShowBoard import ShowBoard
from LeftPieces import UpdatePieceList
from PlacePiece import PlacePiece, PlacePieceByComputer
from PieceInput import TakePieceInput
from CheckBoard import CheckBoard
from Ending import Ending


# --- MAIN ---

print("You chose to play PvE (Person versus Environment/Computer)")
time.sleep(2)

if random.randint(0, 1) == 0:
    print("\n--- The computer starts ---")
    ShowBoard()
    PlayerChoosesPiece = False
    
else:
    print("\n--- You start ---")
    ShowBoard()
    PlayerChoosesPiece = True


IsOver = False                      # Flag used to break out of the main loop
Status = 3                          # if this value us unchanged, it is a draw

for Counter in range(16):
    if PlayerChoosesPiece:
        Piece = TakePieceInput()    # Player either chooses a piece for opponent or says "Quarto" if he believes he can win
        while (Piece == "Quarto"):
            if (CheckBoard()):      # If a Quarto is present on the board, the current player wins, else play continues
                globals.Status = 4
                IsOver = True
                break               # Needed as value of Piece doesn't actually change, i.e. loop wouldn't be exited
            else:                   # I.e. player called Quarto incorrectly, play proceeds after player enters a valid piece
                print("")
                print("There was no Quarto!")
                Piece = TakePieceInput()
        
        if IsOver:
            break

        PlacePieceByComputer(Piece)
        # print("Showing Board 1")
        ShowBoard()

        if CheckBoard():
            globals.Status = 5      # Computer wins
            break
        PlayerChoosesPiece = False


    else:                           #Player's turn to place 
        Piece = random.choice(globals.LeftPieces)  #Computer chooses a random piece        
        PlacePiece(Piece)           #Player places the random piece
        # print("Showing board 2")
        ShowBoard()
        PlayerChoosesPiece = True
    


    UpdatePieceList(Piece)          # Only executed when Piece is for sure on the LeftPieces list (previous loop ensures this)

Ending(globals.Status)              # Finally, when game is over, a final message is output based on the result

