# This file was written by Vakaris

import globals
from LeftPieces import UpdatePieceList

def TakeFirstInput():
    print(f"Possible pieces: {globals.LeftPieces}")
    Prompt = "Choose your first piece (e.g. LHSN): "
    FirstPiece = input(Prompt)
    while not (FirstPiece in globals.LeftPieces):
        FirstPiece = input("Invalid input, try again: ")
    UpdatePieceList(FirstPiece)
    return FirstPiece


# This function is used to make the very first user input, as it's different from others
# The one to go move first chooses the initial piece too
# Returned value FirstPiece is then used in PlacePiece to update the board