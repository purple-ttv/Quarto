# This file was written by Vakaris

import globals

def TakePieceInput():
    print(f"Possible pieces: {globals.LeftPieces}")
    Piece = input("Choose the piece for your opponent to place, or say 'Quarto': ")
    while not (Piece in globals.LeftPieces) and (Piece != "Quarto"):
        Piece = input("Invalid input, try again")
    # The value will only be accepted if it is one of the available values or == Quarto
    return Piece


# This function is called at the end of a player's move to choose the piece for the opponent
# The returned value Piece is then used in PlacePiece to allocate it on the board