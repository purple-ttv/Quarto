# This file was written by Vakaris

import globals
from LeftPieces import UpdatePieceList

def TakePieceInput():
    print(f"Possible pieces: {globals.LeftPieces}")
    Piece = input("Choose the piece for your opponent to place: ")
    UpdatePieceList(Piece)
    return Piece


# This function is called at the end of a player's move to choose the piece for the opponent
# The returned value Piece is then used in PlacePiece to allocate it on the board